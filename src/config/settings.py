TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:postgres@db.localhost:5432/postgres"},
    "apps": {
        "aiohttpdemo_polls": {
            "models": ["aiohttpdemo_polls.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
