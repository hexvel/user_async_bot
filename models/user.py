from tortoise.models import Model
from tortoise import fields


class Users(Model):
    user_id: fields.IntField = fields.IntField(pk=True)
    token: fields.TextField = fields.TextField(default="None")
    balance: fields.IntField = fields.IntField(default=0)
    squad: fields.TextField = fields.TextField(default="Pinky")
    rank: fields.IntField = fields.IntField(default=1)
    username: fields.TextField = fields.TextField(default="User")
    prefix_command: fields.TextField = fields.TextField(default=".х")
    prefix_script: fields.TextField = fields.TextField(default=".с")
    prefix_admin: fields.TextField = fields.TextField(default=".а")
    ignore_list: fields.JSONField = fields.JSONField(default={"users": []})
    trust_list: fields.JSONField = fields.JSONField(default={"users": []})
    profile_photo: fields.TextField = fields.TextField(
        default="photo-212239786_457239018")


class Scripts(Model):
    user_id: fields.IntField = fields.IntField(pk=True)
    recommendation: fields.BooleanField = fields.BooleanField(default=False)
    auto_farm: fields.BooleanField = fields.BooleanField(default=False)
    auto_status: fields.BooleanField = fields.BooleanField(default=False)
    auto_cover: fields.BooleanField = fields.BooleanField(default=False)
    cover_id: fields.IntField = fields.IntField(default=1)
