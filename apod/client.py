import functools

from datetime import datetime

from gql import Client
from gql.dsl import DSLQuery, DSLSchema, dsl_gql
from gql.transport.aiohttp import AIOHTTPTransport

from .webhook import ApodHook
from utils.config import get_client_cfg
from utils.logging import wrap, entering, exiting, get_logger

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
def get_apod_client():
    """ Gets the client to access the API wrapper and caches it """
    return ApodClient()


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
    def __init__(self):
        """ Initializes the client for the API wrapper """
        self._config = get_client_cfg()

        self._hook = ApodHook()
        self._transport = AIOHTTPTransport(url=self._config['endpoint'])
        self._client = Client(transport=self._transport, fetch_schema_from_transport=True)

    @wrap(entering, exiting)
    def _get_schema(self):
        """ Gets GQL schema """
        return DSLSchema(self._client.schema)

    @wrap(entering, exiting)
    async def handle(self, commands):
        """ Handles commands and queries the API wrapper """
        # TODO: Implement full command handling
        if commands['date']:
            result = await self.query_apod_by_date(date=commands['date'])
            query = 'apodByDate'

        else:
            result = await self.query_today()
            query = 'today'

        await self._hook.fire(data=result[query], multi=isinstance(result[query], list))

    @wrap(entering, exiting)
    async def query_today(self, thumbs=False):
        """ Queries the API wrapper with the 'today' query """
        async with self._client as session:
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
    async def query_apod_by_date(self, date, thumbs=False):
        """ Queries the API wrapper with the 'apodByDate' query """
        async with self._client as session:
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
    async def query_apods_by_date(self, start_date, end_date, thumbs=False):
        """ Queries the API wrapper with the 'apodsByDate' query """
        async with self._client as session:
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
    async def query_random_apods(self, count, thumbs=False):
        """ Queries the API wrapper with the 'randomApods' query """
        async with self._client as session:
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
