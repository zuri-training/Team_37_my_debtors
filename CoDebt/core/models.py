from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    username= None
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True, verbose_name='Email Address', max_length=255)
    is_student=models.BooleanField(default=False)
    is_school_admin=models.BooleanField(default=False)
    is_guardian=models.BooleanField(default=False)
    school_name=models.CharField()
    #display_picture=models.URLField(max_length=100, default='')

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    class Meta:  
        ordering= ['email']
        verbose_name= 'User'

    def __str__(self):
        return self.email


class Debtors(models.Model):
    posted_by=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    school_name=models.CharField(max_length=100)
    student_id=models.CharField(max_length=20, unique=True)
    outstanding_fees=models.PositiveIntegerField()
    is_contending_debt=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name,self.last_name


class Comment(models.Model):
    user_commenting=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_on=models.ForeignKey(Debtors, on_delete=models.CASCADE)
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:10]


class Contention(models.Model):
    user_contending=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contending_on=models.ForeignKey(Debtors, on_delete=models.CASCADE)
    reason= models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    evidence=models.FileField()

    def __str__(self):
        return self.contending_on