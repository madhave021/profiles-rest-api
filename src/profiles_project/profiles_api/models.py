from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
             raise ValueError('user must Enter email')
        email=self.normalize_email(email)
        user=self.models(email=email,name=name)

        user.set_password(pssword)
        user.save(using=django._db)

        return user
    def create_superuser(self,name,email,password):
        user=self.create_user(name,email,passsword)

        user.is_superuser=True
        user.is_staff= True
        user.save(using=self_.db)
class UserProfile(AbstractBaseUser,PermissionsMixin):

    """Represent a "user profile" inside your system"""

    email = models.EmailField(max_length=255,unique=True)
    name  = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email
