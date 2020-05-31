import os

from aiohttp import web
from tartiflette_aiohttp import register_graphql_handlers
from tortoise import Tortoise

from config import settings
from aiohttpdemo_polls.routes import setup_routes


async def init_connection(_=None):
    await Tortoise.init(
        db_url=settings.POSTGRES_URL,
        modules={'aiohttpdemo_polls': ['aiohttpdemo_polls.models']}
    )


async def close_connection(_=None):
    await Tortoise.close_connections()


if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    app.on_startup.append(init_connection)
    app.on_cleanup.append(close_connection)

    web.run_app(
        register_graphql_handlers(
            app=app,
            engine_sdl=os.path.join(settings.BASE_DIR, 'aiohttpdemo_polls', 'graphql', 'sdl'),
            engine_modules=[
                "aiohttpdemo_polls.graphql.query_resolvers",
                "aiohttpdemo_polls.graphql.mutation_resolvers",
                "aiohttpdemo_polls.graphql.subscription_resolvers",
                "aiohttpdemo_polls.graphql.directives.rate_limiting",
                "aiohttpdemo_polls.graphql.directives.auth",
            ],
            executor_http_endpoint="/graphql",
            executor_http_methods=["POST"],
            graphiql_enabled=True,
            subscription_ws_endpoint="/ws",
        )
    )
