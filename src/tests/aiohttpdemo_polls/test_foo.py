import datetime

import pytest
from aiohttpdemo_polls.models import Question


async def foo_bar_async():
    return 1


@pytest.mark.asyncio
async def test_bar():
    t = await foo_bar_async()
    assert 1 == t


@pytest.mark.asyncio
async def test_create():
    await Question.create(question_text='foo', max_date=datetime.datetime.now().date())
    count = await Question.all().count()
    assert count == 1


@pytest.mark.asyncio
async def test_create_2():
    await Question.create(question_text='foo', max_date=datetime.datetime.now().date())
    count = await Question.all().count()
    assert count == 1
