from django.contrib import admin

# Register your models here.
from core.models import CustomUser, Debtor, Comment, Contention, SchoolDetail

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Debtor)
admin.site.register(Comment)
admin.site.register(Contention)
admin.site.register(SchoolDetail)