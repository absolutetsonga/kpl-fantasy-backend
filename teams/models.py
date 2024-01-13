from django.db import models

# Create your models here.

# Team -> Players:
# One -> Many

class Team(models.Model): 
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField()

    def __str__(self):
        return f"Team {self.name}"
