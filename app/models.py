from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    password = models.CharField(max_length=16)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    def __str__(self):
        return self.email

# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import UserManager
# from django.db import models
#
#
# # Create your models here.
# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='Email',
#         max_length=255,
#         unique=True,
#     )
#     name = models.CharField(max_length=200)
#     is_active = models.BooleanField(default=False)
#     name = models.CharField(max_length=50)
#     username = models.CharField(max_length=50)
#     password = models.CharField()
#     otp = models.CharField(max_length=6)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'tc']
#
#     def __str__(self):
#         return self.email
