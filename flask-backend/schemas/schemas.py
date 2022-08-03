from flask_marshmallow import Schema
from marshmallow.fields import Str


class IndexSchema(Schema):
    class Meta:
        fields = ("message", "description")

    message = Str(dump_only=True)
    description = Str(dump_only=True)


class InfoSchema(Schema):
    class Meta:
        fields = ("id", "object_hash", "message")

    id = Str(dump_only=True)
    object_hash = Str(dump_only=True)
    message = Str(dump_only=True)


class ImageSchema(Schema):
    class Meta:
        fields = ("message", "name", "filetype", "size", "shape")

    message = Str(dump_only=True)
    name = Str(dump_only=True)
    filetype = Str(dump_only=True)
    size = Str(dump_only=True)
    shape = Str(dump_only=True)
