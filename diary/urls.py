from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.list_pages, name="list"),
    path("list/<int:pid>/", views.list_pages, name="list_page"),
    path("create/", views.create_page, name="create_page"),
]