import asyncio
import os

import pytest
from tortoise.contrib.test import finalizer
from tortoise.contrib.test import initializer
from tortoise.transactions import in_transaction, current_transaction_map

import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import APP_LABEL, POSTGRES_URL


class GetMock:
    def __init__(self, instance):
        self.instance = instance

    def get(self):
        if callable(self.instance):
            raise self.instance()
        return self.instance


class AccessDeniedDBException(Exception):
    def __str__(self):
        return "You should use the 'db' fixture to get access to the database"


real_connection = None
access_denied_getter = None
_LOOP = asyncio.get_event_loop()


@pytest.fixture
def event_loop(request):
    global _LOOP
    """Create an instance of the default event loop for each test case."""
    yield _LOOP


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    global real_connection
    global access_denied_getter
    initializer(
        ["aiohttpdemo_polls.models"],
        loop=_LOOP,
        db_url=POSTGRES_URL,
        app_label="aiohttpdemo_polls",
    )
    real_connection = current_transaction_map[APP_LABEL]
    access_denied_getter = GetMock(AccessDeniedDBException)
    current_transaction_map[APP_LABEL] = access_denied_getter
    request.addfinalizer(finalizer)


@pytest.fixture
async def db(request):
    # this setup works for tests that are running 1 at a time
    is_async = request.node.get_closest_marker('asyncio')
    if not is_async:
        return

    current_transaction_map[APP_LABEL] = real_connection
    transaction = in_transaction(connection_name=APP_LABEL)
    connection = await transaction.__aenter__()
    current_transaction_map[APP_LABEL] = GetMock(connection)
    yield
    current_transaction_map[APP_LABEL] = access_denied_getter
    await connection.rollback()
    # this should be called if the tests are running on multiple threads, for now there's no problem
    # await transaction.__aexit__(None, None, None)
