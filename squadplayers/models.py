from django.db import models

from squads.models import Squad
from players.models import Player

# Create your models here.

# One-to-Many -> Many-to-Many -> Many-to-One
# Squad       -> SquadPlayer  -> Player

# Create your models here.

class SquadPlayer(models.Model):
    class PositionChoices(models.TextChoices):
        GOALKEEPER = 'GK', 'Goalkeeper'
        LEFT_DEFENDER = 'LD', 'Left Defender'
        LEFT_CENTER_DEFENDER = 'LCD', 'Left Center Defender'
        RIGHT_CENTER_DEFENDER = 'RCD', 'Right Center Defender'
        RIGHT_DEFENDER = 'RD', 'Right Defender'
        LEFT_MIDFIELDER = 'LM', 'Left Midfielder'
        CENTER_MIDFIELDER = 'CM', 'Center Midfielder'
        RIGHT_MIDFIELDER = 'RM', 'Right Midfielder'
        LEFT_STRIKER = 'LS', 'Left Striker'
        CENTER_STRIKER = 'CS', 'Center Striker'
        RIGHT_STRIKER = 'RS', 'Right Striker'
        SUBSTITUTE_GOALKEEPER = 'SGK', 'Substitute Goalkeeper'
        SUBSTITUTE_DEFENDER = 'SD', 'Substitute Defender'
        SUBSTITUTE_MIDFIELDER = 'SM', 'Substitute Midfielder'
        SUBSTITUTE_STRIKER = 'SS', 'Substitute Striker'
    
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    position = models.CharField(max_length=255, choices=PositionChoices.choices, blank=False)

    is_captain = models.BooleanField(default=False)
    is_vice_captain = models.BooleanField(default=False)
    on_bench = models.BooleanField(default=False)

    class Meta:
        unique_together = [['squad', 'player']]

    def __str__(self):
        return f"Squad Player {self.player} from {self.squad}"