from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("homepage", views.homepage, name="homepage"),
    path("settings", views.settings, name="settings"),
    path("housetype_library", views.htl, name="htl"),
    path("tables/bootstrap_htmx", views.table_page, name="table_page")
]