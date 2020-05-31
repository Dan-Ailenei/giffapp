import os

POSTGRES_USER = "postgres"
POSTGRES_DATABASE = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_PORT = 5432
POSTGRES_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db.localhost:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URL},
    "apps": {
        "aiohttpdemo_polls": {
            "models": ["aiohttpdemo_polls.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
