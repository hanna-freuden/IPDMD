from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.BeforeEnd, {'water': 1, 'known_others': 1, 'known_from': 1})
        yield (pages.MyPage)
