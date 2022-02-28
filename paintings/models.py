from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.


class Painting(TimeStampedModel):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(
        "User", related_name="paintings", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="paintings")

    def __str__(self):
        return self.title

    def created_string(self):
        time = datetime.now() - self.created
        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created.date()
            return str(time.days) + "일 전"
        else:
            return False


class Like(TimeStampedModel):
    paint = models.ForeignKey(Painting, related_name="likes", on_delete=models.CASCADE)
    owner = models.ForeignKey("User", related_name="likes", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["paint", "owner"], name="unique_owner_paint"
            )
        ]

    def __str__(self):
        return f"paint : {self.paint} - owner : {self.owner}"


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", default="avatars/sparta.png")
