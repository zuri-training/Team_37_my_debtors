from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('studentprofile/<str:pk>', views.studentprofile, name='studentprofile'),
]
