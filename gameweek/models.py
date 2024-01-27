from django.db import models
from datetime import datetime

# Create your models here.

# Gameweek -> GameWeekStats: 
# One    -> Many

class GameWeek(models.Model):
    number = models.IntegerField(unique=True)

    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    first_game = models.DateTimeField(null=True)
    last_game = models.DateTimeField(null=True)

    @property
    def is_active(self):
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    @classmethod
    def current_gameweek(cls):
        now = datetime.now()
        return cls.objects.filter(start_date__lte=now, end_date__gte=now).first()

    def __str__(self):
        return f"Game Week {self.number}"
    
