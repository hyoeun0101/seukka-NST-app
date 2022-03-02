from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Painting, User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
# Create your views here.


def sign_up_or_in(request):
    if request.user.is_authenticated:
        return redirect(reverse("paintings:home"))
    # most_liked_paint = Painting.objects.all().order_by("-like_count")[0].painting
    return render(request, "sign_up_or_in.html")


@method_decorator(login_required, name="dispatch")
class HomeView(ListView):
    model = Painting
    template_name = "home.html"
    ordering = "-created"

    def get_ordering(self):
        ordering = self.request.GET.get("ordering", "-created")
        # validate ordering here
        return ordering


# def home(request):
#     paintings = Painting.objects.all()
#     return render(request, "home.html", {"paintings": paintings})




@login_required(login_url="/")
def create(request):
    if request.method == "POST":
        img_file = request.FILES['img']
        img_file.name = request.POST['title']
        Painting.objects.create(owner_id=request.user.id, image=img_file)
        return JsonResponse({"msg": "success"})
    return render(request, "create.html")


@login_required(login_url="/")
def mypage(request, username):
    try:
        user = User.objects.get(username=username)
        paintings = user.paintings.all()
        return render(request, "mypage.html", {"paintings": paintings, "user": user})
    except User.DoesNotExist:
        return render(request, "404.html")


def log_out(request):
    print("hi")
    if request.user.is_authenticated:
        print("ho")
        logout(request)
    return redirect(reverse("paintings:sign_up_or_in"))
