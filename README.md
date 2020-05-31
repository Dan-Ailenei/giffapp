# Steps:
Install poetry. I just installed it from the command line with dnf, but if that doesn't work for you, you can follow these instructions: https://python-poetry.org/docs/

Install `cmake` and `g++`, these utilities are used to install tartiflette (the graphql library).

Make sure you have python3.8 installed. Run `poetry install` in the root of the project. Poetry is supposed to detect the path to the python version specified in `pyproject.toml` and to create a virtualenv for you. Sometimes it fails tho. You can use the `poetry env use $PATH` where $PATH is the path to a predefined python environment (I use pyenv to create python environments).

At this point I `hope` that everything worked smoothly. To jump into the env in the command line you can use the `poetry shell` command. If you want to configure pycharm to use the poetry env, run `poetry env list --full-path` and use that environment to configure pycharm.

The application is configured to work with postgres. I'm to lazy to install postgress on my own machine so I just added a docker image in the docker directory. Jump into it and run `docker-compose up -d`. The database should be up.

Jump into the src directory and run `aerich upgrade`. This command should run migrations.

To add something into the database and to get a feeling of how things are working you can jump into `ipython` and run the following code:

```python
import datetime
from main import init_connection
from aiohttpdemo_polls.models import Question

async def create_some_data(): 
    await init_connection() 
    await Question.create(question_text='foo', max_date=datetime.datetime.now().date()) 

from tortoise import run_async
run_async(create_some_data())
```
Exit ipython.

Run `main.py` and the server should be running. Go in your browser at http://localhost:8080 and you should see some weird json representation of the question you just created.

You can also go to http://localhost:8080/graphiql and run the following query:
```graphql
subscription {
  launchAndWaitCookingTimer(id: 1) {
    remainingTime
    status
  }
}
```