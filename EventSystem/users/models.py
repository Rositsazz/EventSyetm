from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from .managers import UserManager


class BaseUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)



    # avatar = ImageCropField(blank=True, null=True)
    # full_image = ImageCropField(upload_to='avatars/', blank=True, null=True)
    # cropping = ImageRatioField('full_image', '300x300')
    #
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    #
    # objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Organiser(BaseUser):
    signature = models.ImageField(upload_to="teachers_signatures", null=True,
                                  blank=True)

    def __str__(self):
        return "{0) - {1}".format(self.full_name, self.email)
