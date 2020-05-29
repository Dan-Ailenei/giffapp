from aiohttp import web

from aiohttpdemo_polls.routes import setup_routes
from aiohttpdemo_polls.settings import config

app = web.Application()
setup_routes(app)
app['config'] = config
web.run_app(app)
