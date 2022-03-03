from typing import Tuple
from django.db import IntegrityError
from django.db.models import F
from ninja import Router, Form,File
from ninja.files import UploadedFile

from paintings.models import Like, Painting
from paintings.schema import MessageSchema, PaintSchema

router = Router(tags=["Paint"])


@router.post("/like/{paint_id}", response={200: MessageSchema, 404: MessageSchema})
def create_or_remove_like(request, paint_id: int) -> Tuple[int ,dict]:
    user = request.user
    try:
        paint = Painting.objects.get(pk=paint_id)
        Like.objects.create(owner=user, paint=paint)
        paint.like_count = F("like_count") + 1
        paint.save()
        # for like in user.likes.all():
        #     if like.paint == paint:
        #         like.delete()
        #         return {"msg": "cancle"}
        # Like.objects.create(paint=paint, owner=user)
        return 200, {"msg": "ok"}
    except Painting.DoesNotExist:
        return 404, {"msg": "err"}
    except IntegrityError:
        like = Like.objects.get(owner=user, paint=paint)
        paint.like_count = F("like_count") - 1
        paint.save()
        like.delete()
        return 200, {"msg": "delete"}


@router.post("/create", response={200: MessageSchema, 404: MessageSchema})
def create_paint(request, paint_request: PaintSchema = Form(...), img: UploadedFile = File(...)) -> Tuple[int ,dict]:
    try:
        user = request.user
        upload_img = img.read()
        print(upload_img)
        Painting.objects.create(title=paint_request.title, owner= user, upload_image=upload_img,image=paint_request.painting, style=paint_request.style)
        return 200, {'msg': 'ok'}
    except:
        return 404, {'msg': 'fail'}





@router.delete("/delete/{paint_id}", response={200: MessageSchema, 404: MessageSchema})
def create_paint(request, paint_id: int) -> Tuple[int ,dict]:
    try:
        paint = Painting.objects.get(id=paint_id)
        if request.user == paint.owner:
            paint.delete()
            return 200, {"msg": "delete"}
        else:
            return 404, {"msg": "err-user"}
    except Painting.DoesNotExist:
        return 404, {"msg": "not founded"}
