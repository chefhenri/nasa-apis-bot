from gql import Client
from gql.dsl import DSLQuery, DSLSchema, dsl_gql
from gql.transport.aiohttp import AIOHTTPTransport

from .webhook import ApodHook
from utils.config import get_client_cfg


# TODO: Decorate with logging
class ApodClient:
    def __init__(self, logger):
        self._config = get_client_cfg()
        self._logger = logger

        self._hook = ApodHook(logger=self._logger)
        self._transport = AIOHTTPTransport(url=self._config['endpoint'])
        self._client = Client(transport=self._transport, fetch_schema_from_transport=True)

        self._logger.debug(f'''
        ApodClient initialized; 
        transport: {self._transport},
        client: {self._client},
        hook: {self._hook}
        ''')
        self._logger.info('ApodClient initialized')

    def _get_schema(self):
        return DSLSchema(self._client.schema)

    async def handle(self, commands):
        self._logger.debug(f'Commands: {commands}')

        # TODO: Implement full command handling
        if commands['date']:
            result = await self.query_apod_by_date(date=commands['date'])
            query = 'apodByDate'
        else:
            result = await self.query_today()
            query = 'today'

        self._logger.info(f'Query set to "{query}"')
        self._logger.info('Query results received')
        self._logger.debug(f'Query results: {result}')

        await self._hook.fire(data=result[query], multi=isinstance(result[query], list))

    async def query_today(self, thumbs=False):
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

    async def query_apod_by_date(self, date, thumbs=False):
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

    async def query_apods_by_date(self, start_date, end_date, thumbs=False):
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

    async def query_random_apods(self, count, thumbs=False):
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
