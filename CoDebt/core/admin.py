from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser, Debtors, Comment, Contention

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Debtors)
admin.site.register(Comment)
admin.site.register(Contention)