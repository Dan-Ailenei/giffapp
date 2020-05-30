from tortoise.models import Model
from tortoise import fields

# db = PostgresqlDatabase('')

# class BaseModel(Model):
#     class Meta:
#         database = db


class Question(Model):
    question_text = fields.CharField(max_length=200)
    max_date = fields.DateField()


class Choice(Model):
    choice_text = fields.CharField(max_length=200)
    votes = fields.IntField()
    question = fields.ForeignKeyField('diff_models.Question')


# db.connect()
