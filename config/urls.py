"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from paintings.routers import paints_router, users_router

api = NinjaAPI()
api.add_router("/users/", users_router)
api.add_router("/paints/", paints_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("paintings.urls", namespace="paintings")),
    path("api/", api.urls),
]


# settings를 사용하려면 이렇게 사용해야함. 장고가 그렇게 하라고 했기때문

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
