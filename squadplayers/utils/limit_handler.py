from core.constants import SQUAD_MAX_LIMITS

class LimitChecker:
    def exceeds_limit(self, players):
        raise NotImplementedError

class TotalLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["TOTAL"]

    def exceeds_limit(self, players):
        return players.count() >= self.LIMIT

class OnBenchLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["ON_BENCH"]

    def exceeds_limit(self, players):
        return players.filter(on_bench=True).count() >= self.LIMIT

class CaptainLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["CAPTAIN"]

    def exceeds_limit(self, players):
        return players.filter(is_captain=True).count() >= self.LIMIT

class ViceCaptainLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["VICE_CAPTAIN"]

    def exceeds_limit(self, players):
        return players.filter(is_vice_captain=True).count() >= self.LIMIT

class GoalkeepersLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["GOALKEEPER"]

    def exceeds_limit(self, players):
        return players.filter(player_id__position="Goalkeeper").count() >= self.LIMIT
    
class DefendersLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["DEFENDER"]

    def exceeds_limit(self, players):
        return players.filter(player_id__position="Defender").count() >= self.LIMIT
    
class MiddlefieldersLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["MITTELFELD"]

    def exceeds_limit(self, players):
        return players.filter(player_id__position="Mittelfeld").count() >= self.LIMIT

class StrikersLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["STRIKER"]

    def exceeds_limit(self, players):
        return players.filter(player_id__position="Striker").count() >= self.LIMIT
    
class OneClubPlayersLimitChecker(LimitChecker):
    LIMIT = SQUAD_MAX_LIMITS["FROM_ONE_CLUB"]

    def exceeds_limit(self, players, player):
        return players.filter(player__club=player.club).count() >= self.LIMIT
    
class EnoughBudgetLimitChecker(LimitChecker):
    def exceeds_limit(self, total_budget, player_price):
        return total_budget < player_price

    