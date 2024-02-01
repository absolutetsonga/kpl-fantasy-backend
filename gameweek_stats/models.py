from django.db import models

from squadplayers.models import SquadPlayer
from gameweek.models import GameWeek

# Create your models here.

# Player -> GameWeekStats: 
# One    -> Many

class GameWeekStats(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    squad_player = models.ForeignKey(SquadPlayer, on_delete=models.CASCADE, related_name="gameweek_stats")
    gameweek = models.ForeignKey(GameWeek, on_delete=models.CASCADE, related_name="player_stats")

    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    own_goals_scored = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    is_captain = models.BooleanField(default=False)
    is_vice_captain = models.BooleanField(default=False)
    on_bench = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.gameweek} Stats of {self.squad_player}"
