from django.db import models

from players.models import Player
from gameweek.models import GameWeek

# Create your models here.

# Player -> GameWeekStats: 
# One    -> Many

class GameWeekStats(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="gameweek_stats")
    gameweek = models.ForeignKey(GameWeek, on_delete=models.CASCADE, related_name="player_stats")

    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    own_goals_scored = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.gameweek} Stats of {self.player}"
