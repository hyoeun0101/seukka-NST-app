from django.views.generic import ListView
from django.shortcuts import render
from .models import Painting, User
from django.core.paginator import InvalidPage


# Create your views here.


def sign_up_or_in(request):
    if request.method == "GET":
        if User.is_authenticated:
            return render(request, "home.html")
        return render(request, "sign_up_or_in.html")

class HomeView(ListView):
    model = Painting
    template_name = "home.html"
    ordering = "-created"
    paginate_by = 3


def home(request):
    paintings = Painting.objects.all()
    return render(request, "home.html", {"paintings": paintings})


def create(request):
    return render(request, "create.html")


def mypage(request, username):
    try:
        user = User.objects.get(username=username)
        paintings = user.paintings.all()
        return render(request, "mypage.html", {"paintings": paintings, "user": user})
    except User.DoesNotExist:
        return render(request, "404.html")
