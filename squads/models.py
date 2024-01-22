from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

# One-to-One Relationship
# User -> Squad

User = get_user_model()

class Squad(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="squad")

    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    total_budget = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"Squad of {self.user}"