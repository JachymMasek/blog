from django.urls import path
from . import views

urlpatterns = [
    # Statické stránky
    path("",         views.home,    name="home"),
    path("about/",   views.about,   name="about"),
    path("contact/", views.contact, name="contact"),

    # Auth
    path("login/",  views.login_view,  name="login"),
    path("logout/",   views.logout_view,   name="logout"),
    path("register/", views.register_view, name="register"),

    # Blog CRUD
    path("blog/",                    views.article_list,   name="article_list"),
    path("blog/new/",                views.article_create, name="article_create"),
    path("blog/<slug:slug>/",        views.article_detail, name="article_detail"),
    path("blog/<slug:slug>/edit/",   views.article_update, name="article_update"),
    path("blog/<slug:slug>/delete/", views.article_delete, name="article_delete"),
]