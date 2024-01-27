from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from .managers import CustomUserManager

# use the get_user_model() method from django.contrib.auth to refer 

class CustomUser(AbstractUser):
    username = models.CharField(
        _('username'), 
        max_length=150, 
        unique=True, 
        blank=True, 
        null=True, 
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'), 
        validators=[UnicodeUsernameValidator()], error_messages={
            'unique': _("A user with that username already exists")
    })
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    has_draft = models.BooleanField(default=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"User email: {self.email}"
