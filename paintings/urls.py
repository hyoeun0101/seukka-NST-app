from django.urls import path

from . import views as pt_views

app_name = "paintings"
urlpatterns = [
    path("", pt_views.sign_up_or_in, name="sign_up_or_in"),
    path("home/", pt_views.HomeView.as_view(), name="home"),
    path("create/", pt_views.create, name="create"),
    path("logout/", pt_views.log_out, name="logout"),
    path("avatar/", pt_views.avatar, name="avatar"),
    path("<str:username>/", pt_views.mypage, name="mypage"),
]
