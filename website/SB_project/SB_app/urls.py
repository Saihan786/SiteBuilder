from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("homepage", views.homepage, name="homepage"),
    path("settings", views.settings, name="settings"),
    path("housetype_library", views.htl, name="htl"),
    path("block_builder", views.block_builder, name="block_builder"),
]