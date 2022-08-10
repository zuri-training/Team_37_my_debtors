"""CoDebt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('register/', core_views.register, name='register'),
    path('guardian/', core_views.guardian, name= 'guardian'),
     path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'forgottenpassword.html'), 
          name='reset_password'),
     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'checkyourmail.html'),
         name="password_reset_done"),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView. as_view(template_name = 'confirmedpassword.html'),
         name='password_reset_confirm'),
     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'passwordreset.html' ),
         name='password_reset_complete'),        

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
