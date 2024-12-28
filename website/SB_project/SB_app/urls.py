from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("example", views.bad_example, name="example"),
    path("homepage", views.homepage, name="homepage"),
    path("settings", views.settings, name="settings"),
    path("housetype_library", views.htl, name="htl"),
]