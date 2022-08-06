from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path("comment/", views.make_comment, name="comment"),
]
