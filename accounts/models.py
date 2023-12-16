from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager
from accounts.validators import validate_name, validate_username
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(max_length=50,
                                unique=True,
                                help_text=_(
                                    "Requered. 50 characters or fewer. English letters in lowercase,"
                                    " or underscore"
                                ),
                                validators=[validate_username])
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=50, validators=[validate_name])
    last_name = models.CharField(max_length=50, validators=[validate_name])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.username = self.username.lower()
        super().save(*args, **kwargs)



