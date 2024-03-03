from players.models import Player
from squads.models import Squad

from datetime import datetime
from gameweek.models import GameWeek

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

        except Player.DoesNotExist or Squad.DoesNotExist:
            return error_handler.bad_request_error('Игрок или Драфт не найден.')
            
        for key, checker in checkers.items():
            if key == 'total' and checker.exceeds_limit(players):
                return error_handler.bad_request_error('Команда полностью собрана.')

            if key == 'on_bench' and data.get('on_bench') == True and checker.exceeds_limit(players):
                return error_handler.bad_request_error('Слишком много игроков на замене.')

            if key == 'captain' and data.get('is_captain') == True and checker.exceeds_limit(players):
                return error_handler.bad_request_error('В команде уже есть капитан.')

            if key == 'vice_captain' and data.get('is_vice_captain') == True and checker.exceeds_limit(players):
                return error_handler.bad_request_error('В команде уже есть вице-капитан.')

            if key == 'goalkeeper' and data.get('position') == 'Goalkeeper' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'Вы не можете иметь больше {checker.LIMIT} вратарей в команде.')
            
            if key == 'defender' and data.get('position') == 'Defender' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'Вы не можете иметь больше {checker.LIMIT} защитников в команде.')
            
            if key == 'middlefielder' and data.get('position') == 'Mittelfeld' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'Вы не можете иметь больше {checker.LIMIT} полузащитников в команде.')
            
            if key == 'striker' and data.get('position') == 'Striker' and checker.exceeds_limit(players):
                return error_handler.bad_request_error(f'Вы не можете иметь больше {checker.LIMIT} нападающих в команде.')
            
            if key == 'one_club' and checker.exceeds_limit(players, player):
                return error_handler.bad_request_error('Вы не можете иметь больше 3 игроков из одного клуба.')
            
        if not self.is_position_compatible(player.position, position):
            return error_handler.bad_request_error('Позиция игрока не соответствует позиции в вашей команде.')

        if self.is_squad_position_occupied(players, position):
            return error_handler.bad_request_error('Эта позиция уже занята другим игроком команды.')

        if self.player_already_in_squad(squad_id, player_id): 
            return error_handler.bad_request_error('Этот игрок уже есть в команде.')
        
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
            return error_handler.bad_request_error('Игрок или Драфт не найден')

        for key, checker in checkers.items():
            if key == 'enough_budget' and checker.exceeds_limit(total_budget=squad.total_budget, player_price=player.price):
                return error_handler.bad_request_error('Недостаточно бюджета для добавления игрока.')

class SquadGameweekValidationHandler:
    def validate_gameweek_time(self, gameweek):
        if gameweek is not None:
            return error_handler.bad_request_error("Невозможно изменить состав в течение активной игровой недели.")
    
    def validate_gameweek_is_updated(self, gameweek):
        not_updated_gameweeks = GameWeek.objects.filter(end_date__lt=datetime.now(), updated=False)

        if not_updated_gameweeks.exists():
            return error_handler.bad_request_error("Изменения не допускаются до тех пор, пока не будут обновлены все прошлые игровые недели.")


squad_player_validate_handler = SquadPlayerValidationHandler()
squad_budget_validate_handler = SquadBudgetValidationHandler()
squad_gameweek_validate_handler = SquadGameweekValidationHandler()