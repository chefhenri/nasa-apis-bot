import functools
from datetime import datetime

from gql import Client
from gql.dsl import DSLQuery, DSLSchema, dsl_gql
from gql.transport.aiohttp import AIOHTTPTransport

from apod.webhook import get_hook
from utils.config import get_client_cfg
from utils.logging import wrap, entering, exiting

DATE_FMTS = (
    '%m/%d/%Y',
    '%d/%m/%Y',
    '%m.%d.%Y',
    '%d.%m.%Y',
    '%m-%d-%Y',
    '%d-%m-%Y',
    '%Y-%m-%d'
)


@functools.lru_cache(maxsize=None)
@wrap(entering, exiting)
def get_apod_client():
    """ Gets the client to access the API wrapper and caches it """
    config = get_client_cfg()
    hook = get_hook()
    transport = AIOHTTPTransport(url=config['endpoint'])
    gql_client = Client(transport=transport, fetch_schema_from_transport=True)

    return ApodClient(config=config, hook=hook, transport=transport, gql_client=gql_client)


# TODO: Update unit tests
@wrap(entering, exiting)
def convert_date(_date):
    """ Converts and formats the date """
    for fmt in DATE_FMTS:
        try:
            return datetime.strptime(_date, fmt).strftime('%Y-%m-%d')
        except ValueError:
            pass

    raise ValueError('No valid date format found')


class ApodClient:
    def __init__(self, config, hook, transport, gql_client):
        """ Initializes the client for the API wrapper """
        self._config = config
        self._hook = hook
        self._transport = transport
        self._gql_client = gql_client

    @wrap(entering, exiting)
    def _get_schema(self):
        """ Gets GQL schema """
        return DSLSchema(self._gql_client.schema)

    @wrap(entering, exiting)
    async def _get_query(self, commands):
        """ Gets the query result for the provided command """
        # TODO: Implement full command handling
        if commands['date']:
            query = 'apodByDate'
            result = await self._query_apod_by_date(date=commands['date'])
        else:
            query = 'today'
            result = await self._query_today()

        return query, result

    @wrap(entering, exiting)
    async def handle(self, commands):
        """ Handles query commands and fires the webhook """
        query, result = self._get_query(commands)
        await self._hook.fire(data=result[query], multi=isinstance(result[query], list))

    @wrap(entering, exiting)
    async def _query_today(self, thumbs=False):
        """ Queries the API wrapper with the 'today' query """
        async with self._gql_client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.today(apiKey=self._config['api_key'], thumbs=thumbs).select(
                    schema.Apod.copyright,
                    schema.Apod.explanation,
                    schema.Apod.hdurl,
                    schema.Apod.mediaType,
                    schema.Apod.title,
                    schema.Apod.url
                )
            ))

            result = await session.execute(query)
            return result

    @wrap(entering, exiting)
    async def _query_apod_by_date(self, date, thumbs=False):
        """ Queries the API wrapper with the 'apodByDate' query """
        async with self._gql_client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.apodByDate(apiKey=self._config['api_key'], date=date, thumbs=thumbs).select(
                    schema.Apod.copyright,
                    schema.Apod.explanation,
                    schema.Apod.hdurl,
                    schema.Apod.mediaType,
                    schema.Apod.title,
                    schema.Apod.url
                )
            ))

            result = await session.execute(query)
            return result

    @wrap(entering, exiting)
    async def _query_apods_by_date(self, start_date, end_date, thumbs=False):
        """ Queries the API wrapper with the 'apodsByDate' query """
        async with self._gql_client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.apodsByDate(apiKey=self._config['api_key'], startDate=start_date, endDate=end_date,
                                         thumbs=thumbs).select(
                    schema.Apod.copyright,
                    schema.Apod.explanation,
                    schema.Apod.hdurl,
                    schema.Apod.mediaType,
                    schema.Apod.title,
                    schema.Apod.url
                )
            ))

            result = await session.execute(query)
            return result

    @wrap(entering, exiting)
    async def _query_random_apods(self, count, thumbs=False):
        """ Queries the API wrapper with the 'randomApods' query """
        async with self._gql_client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.randomApods(apiKey=self._config['api_key'], count=count, thumbs=thumbs).select(
                    schema.Apod.copyright,
                    schema.Apod.explanation,
                    schema.Apod.hdurl,
                    schema.Apod.mediaType,
                    schema.Apod.title,
                    schema.Apod.url
                )
            ))

            result = await session.execute(query)
            return result
