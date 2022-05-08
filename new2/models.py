from tortoise import fields
from tortoise.models import Model


class Tasklist(Model):
    task_id = fields.UUIDField(pk=True)
    property= fields.CharField(max_length=400)
    description = fields.CharField(max_length=400)
    date_created_at = fields.DatetimeField(auto_now_add=True)
    complete_task = fields.BooleanField(default=False)

