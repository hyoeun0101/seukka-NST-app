from urllib import response

from django.contrib.auth import authenticate, login, logout, password_validation
from ninja import Form, Router

# from django.contrib.auth.models import User
from paintings.models import User
from paintings.schema import MessageSchema, UserSchema

router = Router(tags=["Users"])


@router.post("/sign", response=MessageSchema)
def sign_up_or_in(request, data: UserSchema = Form(...)):
    user = request.user
    username = data.username
    password = data.password
    try:
        password_validation.validate_password(password, User)
    except Exception as e:
        return {"msg": list(e)[0]}
    try:
        User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user is None:
            return {"msg": "incorrect pw"}
        login(request, user)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
    return {"msg": "ok"}
