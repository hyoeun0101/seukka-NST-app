from typing import Dict

from ninja import Form, Router
from paintings.schema import MessageSchema, UserSchema
from django.contrib.auth import authenticate, login

# from django.contrib.auth.models import User
from paintings.models import User
from django.contrib.auth import password_validation

router = Router(tags=["Users"])


@router.post("/sign", response=MessageSchema)
def sign_up_or_in(request, data: UserSchema = Form(...)) -> Dict:
    username = data.username
    password = data.password
    try:
        # 비밀번호 유효성 검사
        password_validation.validate_password(password, User)
    except Exception as e:
        return {"msg": list(e)[0]}
    try:
        User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        # 아이디, 패스워드 일치하지 않으면
        if user is None:
            return {"msg": "incorrect pw"}
        login(request, user)
    # 유저가 존재하지 않으면
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
    return {"msg": "ok"}
