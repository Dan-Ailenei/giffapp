from aiohttp import web
from tortoise import Tortoise

from config import settings
from aiohttpdemo_polls.routes import setup_routes


async def init_connection(_):
    await Tortoise.init(
        db_url=settings.TORTOISE_ORM['connections']['default'],
        modules={'aiohttpdemo_polls': ['aiohttpdemo_polls.models']}
    )


async def close_connection(_):
    await Tortoise.close_connections()


app = web.Application()
app['config'] = settings.__dict__
setup_routes(app)
app.on_startup.append(init_connection)
app.on_cleanup.append(close_connection)
web.run_app(app)
