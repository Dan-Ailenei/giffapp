import os
import sys

POSTGRES_USER = "giffapp"
POSTGRES_PASSWORD = "giffapp"
POSTGRES_DATABASE = "giffapp"
POSTGRES_PORT = 5432

if 'pytest' in sys.argv[0]:
    POSTGRES_DATABASE = "test_giffapp"

POSTGRES_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db.localhost:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

APP_LABEL = "aiohttpdemo_polls"

TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URL},
    "apps": {
        APP_LABEL: {
            "models": [f"{APP_LABEL}.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
