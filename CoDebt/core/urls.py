from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='home'),
    path('register/school/', views.register_school, name='register_school'),
    path('register/guardian/', views.register_users, name='register_guardian'),
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('contact/', views.contact_us, name='contact'),
    path('about/', views.about_us, name='about'),
    path('my-dashboard/', views.dashboard, name='dashboard'),
    path('students/profiles/<str:pk>/', views.studentprofile, name='profile'),
    path('schools/profiles/<str:pk>/', views.schoolprofiles, name='school_profile'),
    path('search/', views.search, name='search'),
    path('search/<str:pk>/', views.resolve, name='resolve'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('debtors/add/', views.add_debtor, name='add_debtor')
]
