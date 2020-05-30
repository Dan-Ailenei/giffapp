from aiohttp import web

from aiohttpdemo_polls.models import Question


async def index(request):
    questions = await Question.all()
    return web.Response(text=str([q.__dict__ for q in questions]))
