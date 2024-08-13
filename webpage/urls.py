from django.urls import path
from . import views
urlpatterns = [
    path("",  views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name="contact"),
    path("table/", views.table_Page, name="table-page"),
    path("card/", views.cardView, name="card-page"),
    path("color/", views.cardColorPage, name="cardcolor"),
]
