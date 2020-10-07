from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
            yield (pages.Intro)
            yield (pages.Intro2)
            yield (pages.Intro3)
            yield (pages.Intro4)
            yield (pages.Intro6, {'ex_sum_a': 15, 'ex_sum_b': 15, 'ex_back_a': 7.5, 'ex_back_b': 7.5, 'ex_sum':15})
            yield (pages.Intro7, {'ex_sum_a1': 15, 'ex_sum_b1': 15, 'ex_minus1': 7.5, 'ex_minus': 7.5, 'ex_final': 7.5 })
            yield (pages.Intro5)
            yield (pages.Choice, {'contribution_within': 5, 'contribution_between': 5, 'keep': 0})
            yield (pages.Results),
            yield (pages.Expectations, {'exp_own_a': 5, 'exp_own_b': 5, 'exp_other_a': 5, 'exp_other_b': 5})






