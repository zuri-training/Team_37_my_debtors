from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, verbose_name='Email Address', max_length=255)
    is_school_admin = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)
    #avatar = models.ImageField(upload_to='avatar/', default='avatar.svg')
    avatar = CloudinaryField('avatars')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        ordering = ["-email"]
        verbose_name = 'User'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Debtor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='school')
    guardian = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='guardian', null=True, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    current_class = models.CharField(max_length=3)
    student_id = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100)
    debt_type = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    outstanding_fees = models.PositiveIntegerField()
    is_contending_debt = models.BooleanField(default=False)
    #student_picture = models.ImageField(upload_to='student/')
    student_picture = CloudinaryField('student_pictures', blank=True, null=True)

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
    guardian_contending = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    #evidence = models.FileField(upload_to='proof_of_contention/')
    evidence = CloudinaryField('proof_of_contention')

    def __str__(self):
        return self.reason[:50]


class SchoolDetail(models.Model):
    school = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    # copy_of_CAC = models.FileField(upload_to='proof_of_cac/')
    copy_of_CAC = CloudinaryField('proof_of_CAC')
    CAC_number = models.CharField(
        unique=True,
        max_length=10,
        validators=[MinLengthValidator(10, 'CAC Number must be 10 digits')]
    )
    pending_debts = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.school_name