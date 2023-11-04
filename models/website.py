from tortoise.models import Model
from tortoise import fields


class Account(Model):
    user_id = fields.IntField(pk=True)
    number = fields.TextField()
    password = fields.TextField()
    name = fields.TextField()
    surname = fields.TextField()
    username = fields.TextField(default="NickName")
    ref_link = fields.TextField()
    profile_photo_link = fields.TextField(
        default="https://www.pngfind.com/pngs/m/676-6764065_default-profile-picture-transparent-hd-png-download.png")
    is_private = fields.BooleanField(default=False)
    default_lang = fields.TextField(default="ru")
