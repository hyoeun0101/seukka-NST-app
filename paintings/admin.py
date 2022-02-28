from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models as pt_models

# Register your models here.


@admin.register(pt_models.Painting)
class PaintAdmin(admin.ModelAdmin):
    pass


@admin.register(pt_models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(pt_models.User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            "basic_info",
            {
                "fields": ("username", "password", "avatar"),
            },
        ),
    )
    list_display = ("username", "avatar")
