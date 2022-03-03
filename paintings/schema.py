from ninja import Schema


class UserSchema(Schema):
    username: str
    password: str


class MessageSchema(Schema):
    msg: str

class PaintSchema(Schema):
    title: str
    style: str
    painting : str
