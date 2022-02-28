from ninja import Schema


class UserSchema(Schema):
    username: str
    password: str


class MessageSchema(Schema):
    msg: str
