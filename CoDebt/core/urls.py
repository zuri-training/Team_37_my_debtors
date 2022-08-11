from django.urls import path
from core import views

app_name = "core"


urlpatterns = [
    path('', views.index, name='home'),
    path('register/school/', views.register_school, name='register_school'),
    path('register/guardian/', views.register_admin, name='register_guardian'),
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('contact/', views.contact_us, name='contact'),
    path('about/', views.about_us, name='about'),
    path('password-reset/', views.password_reset, name='password-reset'),
    path('my-dashboard/', views.dashboard, name='dashboard'),
    path('profiles/<str:student_id>/', views.studentprofile, name='profile'),
    path('search/', views.search, name='search'),
    path('addDebtor', views.addDebtor, name='addDebtor'),
]
