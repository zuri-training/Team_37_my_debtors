from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('edit/<str:pk>/', views.UpdatePost.as_view(), name='update'),
    path('delete/<str:pk>/', views.DeleteDebtor.as_view(), name='delete'),
]