from players.models import Player
from squads.models import Squad

from core.constants import POSITION_MAPPING

from ..models import SquadPlayer
from utils.error_handler import error_handler

class SquadPlayerValidationHandler:
    def validate_squad_limits(self, players, checkers, data):
        position = data.get('position')

        player_id = data.get('player')
        squad_id = data.get('squad')
        
        try:
            player = Player.objects.get(id=player_id)
            squad = Squad.objects.get(id=squad_id)

        except Player.DoesNotExist or Squad.DoesNotExist:
            return error_handler.bad_request_error('Player or Squad not found.')
            
        for key, checker in checkers.items():
            if key == 'total' and checker.exceeds_limit(players):
                return error_handler.bad_request_error('Squad is full.')

            if key == 'on_bench' and data.get('on_bench') == True and checker.exceeds_limit(players):
                return error_handler.bad_request_error('Too many players on the bench.')

            if key == 'captain' and data.get('is_captain') == True and checker.exceeds_limit(players):
                return error_handler.bad_request_error('Squad already has a captain.')

            if key == 'vice_captain' and data.get('is_vice_captain') == True and checker.exceeds_limit(players):
                return error_handler.bad_request_error('Squad already has a vice-captain.')

            if key == 'goalkeeper' and data.get('position') == 'Goalkeeper' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'You cannot have more than allowed {checker.LIMIT} goalkeepers in a squad.')
            
            if key == 'defender' and data.get('position') == 'Defender' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'You cannot have more than allowed {checker.LIMIT} defenders in a squad.')
            
            if key == 'middlefielder' and data.get('position') == 'Mittelfeld' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'You cannot have more than allowed {checker.LIMIT} middlefielders in a squad.')
            
            if key == 'striker' and data.get('position') == 'Striker' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'You cannot have more than allowed {checker.LIMIT} strikers in a squad.')
            
            if key == 'one_club' and checker.exceeds_limit(players, player):
                return error_handler.bad_request_error('Too many players from the same club in the squad.')
            
        if not self.is_position_compatible(player.position, position):
            return error_handler.bad_request_error('Player position does not match the squad position.')

        if self.is_squad_position_occupied(players, position):
            return error_handler.bad_request_error('This position is already occupied by another squad player.')

        if self.player_already_in_squad(squad_id, player_id): 
            return error_handler.bad_request_error('This player is already in the squad')
        
        return None
    
    def player_already_in_squad(self, squad_id, player_id):
        is_player_exists = SquadPlayer.objects.filter(squad=squad_id, player=player_id).exists()

        return is_player_exists
            
    def is_position_compatible(self, player_position, squad_player_position):        
        valid_positions = POSITION_MAPPING.get(player_position, [])
        return squad_player_position in valid_positions
    
    def is_squad_position_occupied(self, players, squad_player_position):
        return players.filter(position=squad_player_position).exists()
    

class SquadBudgetValidationHandler:
    def validate_squad_budget(self, player, squad, checkers):
        player_id = player.id
        squad_id = squad.id

        try:
            player = Player.objects.get(id=player_id)
            squad = Squad.objects.get(id=squad_id)

        except Player.DoesNotExist or Squad.DoesNotExist:
            return error_handler.bad_request_error('Player or Squad not found.')

        for key, checker in checkers.items():
            if key == 'enough_budget' and checker.exceeds_limit(total_budget=squad.total_budget, player_price=player.price):
                return error_handler.bad_request_error('Insufficient budget to add player.')


squad_player_validate_handler = SquadPlayerValidationHandler()
squad_budget_validate_handler = SquadBudgetValidationHandler()