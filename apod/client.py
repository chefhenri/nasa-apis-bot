from gql import Client
from gql.dsl import DSLQuery, DSLSchema, dsl_gql
from gql.transport.aiohttp import AIOHTTPTransport

from .webhook import ApodWebhook as Webhook


class ApodClient:
    def __init__(self, endpoint, api_key, channel_id, channel_url, logger):
        self.api_key = api_key
        self.transport = AIOHTTPTransport(url=endpoint)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)
        self.hook = Webhook(gql_endpoint=endpoint,
                            api_key=api_key,
                            channel_id=channel_id,
                            channel_url=channel_url,
                            logger=logger)
        self.logger = logger

        self.logger.info('ApodClient initialized')
        self.logger.debug(f'''
        ApodClient initialized; 
        transport: {self.transport},
        client: {self.client},
        hook: {self.hook}
        ''')

    def _get_schema(self):
        return DSLSchema(self.client.schema)

    async def handle(self, commands):
        self.logger.debug(f'Commands: {commands}')

        # TODO: Implement other command handling
        # if commands['count']:
        #     result = await self.query_random_apods(count=commands['count'])
        #     query = 'randomApods'
        # elif commands['start_date']:
        #     result = await self.query_apods_by_date(start_date=commands['start_date'], end_date=commands['end_date'])
        #     query = 'apodsByDate'
        # elif commands['date']:
        #     result = await self.query_apod_by_date(date=commands['date'])
        #     query = 'apodByDate'
        # else:
        #     result = await self.query_today()
        #     query = 'today'

        result = await self.query_today()
        query = 'today'

        self.logger.info(f'Query set to "{query}"')
        self.logger.info('Query results received')
        self.logger.debug(f'Query results: {result}')

        await self.hook.fire(data=result[query], multi=isinstance(result[query], list))

    async def query_today(self, thumbs=False):
        async with self.client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.today(apiKey=self.api_key, thumbs=thumbs).select(
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
        async with self.client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.apodByDate(apiKey=self.api_key, date=date, thumbs=thumbs).select(
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
        async with self.client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.apodsByDate(apiKey=self.api_key, startDate=start_date, endDate=end_date,
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
        async with self.client as session:
            schema = self._get_schema()
            query = dsl_gql(DSLQuery(
                schema.Query.randomApods(apiKey=self.api_key, count=count, thumbs=thumbs).select(
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
