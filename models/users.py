from tortoise.models import Model
from tortoise import fields


class Users(Model):
    user_id = fields.IntField(pk=True)
    rank = fields.IntField(default=1)
    balance = fields.IntField(default=0)
    token = fields.TextField(default="None")
    prefix_commands = fields.TextField(default=".х")
    prefix_scripts = fields.TextField(default=".с")
    prefix_admin = fields.TextField(default=".а")
    nickname = fields.TextField(default="NickName")
    ignore_list = fields.JSONField(default=list)
    trust_list = fields.JSONField(default=list)
    trust_prefix = fields.TextField(default="#")


class Scripts(Model):
    user_id = fields.IntField(pk=True)
    auto_farm = fields.IntField(default=0)
    auto_status = fields.IntField(default=0)
    auto_status_stamp = fields.TextField(default="UTC+3")


class Templates(Model):
    user_id = fields.IntField(pk=True)
    name = fields.TextField()
    message = fields.TextField()
    type = fields.TextField()


class Aliases(Model):
    user_id = fields.IntField(pk=True)
    new_command = fields.TextField()
    command = fields.TextField()
