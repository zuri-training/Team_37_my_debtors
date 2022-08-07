from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, verbose_name='Email Address', max_length=255)
    is_school_admin = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)
    school_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/', default='avatar.svg', null=True,blank=True)
    copy_of_CAC = models.FileField(upload_to='proof_of_cac', default=None, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        ordering = ["-email"]
        verbose_name = 'User'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Debtor(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    outstanding_fees = models.PositiveBigIntegerField()
    is_contending_debt = models.BooleanField(default=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Comment(models.Model):
    user_commenting = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commented_on = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]


class Contention(models.Model):
    debtor_contending = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    evidence = models.FileField(upload_to='proof_of_contention')

    def __str__(self):
        return self.reason[:50]