from django.db import models
from teams.models import Team

# Create your models here.

# Player -> GameWeekStats: 
# One    -> Many

class Player(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)
    club = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255) 
    height = models.CharField(max_length=255) 
    
    age = models.IntegerField() 
    market_value = models.IntegerField()

    image_url = models.URLField()
    nationality_image_url = models.URLField()

    price = models.DecimalField(max_digits=3, decimal_places=1, null=True) 
    points = models.IntegerField(default=0)

    is_injured = models.BooleanField(default=False) 
    is_right_foot = models.BooleanField(default=True)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    sofascore_id = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return f"Player {self.name}"
    
