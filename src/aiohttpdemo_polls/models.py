from tortoise.models import Model
from tortoise import fields


class Question(Model):
    question_text = fields.CharField(max_length=200)
    max_date = fields.DateField()


class Choice(Model):
    choice_text = fields.CharField(max_length=200)
    votes = fields.IntField()
    question = fields.ForeignKeyField('aiohttpdemo_polls.Question', related_name='questions')
