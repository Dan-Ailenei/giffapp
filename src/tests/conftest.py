import asyncio
import os
import pytest
from tortoise.contrib.test import finalizer
from tortoise.contrib.test import initializer
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
_LOOP = asyncio.get_event_loop()


@pytest.fixture
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    yield _LOOP


@pytest.fixture(scope="function", autouse=True)
def initialize_tests(request):
    db_url = os.environ.get("inexistent", "sqlite:///tmp/test-{}.sqlite")
    initializer(["aiohttpdemo_polls.models"], loop=_LOOP, db_url=db_url, app_label="aiohttpdemo_polls")
    request.addfinalizer(finalizer)
