from django.db import models
from gameweek.models import GameWeek
from teams.models import Team

class Game(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    gameweek = models.ForeignKey(GameWeek, on_delete=models.CASCADE, related_name='games')

    home_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="home_game_id")
    away_team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="away_game_id")

    home_score = models.IntegerField(null=True, default=-1)
    away_score = models.IntegerField(null=True, default=-1)

    sofascore_id = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return f"Game: {self.home_team.name} VS {self.away_team.name}"
