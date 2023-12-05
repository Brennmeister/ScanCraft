from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thumbnail", views.thumbnail, name="thumbnail"),
    path("upload", views.upload, name="upload"),
]
