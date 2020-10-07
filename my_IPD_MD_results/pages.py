from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

        # variables for template
        # ----------------------------------------------------------------------------------------------------------------
        def vars_for_template(self):
            return {

                'contribution_within': self.participant.vars['contribution_within'],
                'contribution_between': self.participant.vars['contribution_between'],
                'keep': self.participant.vars['keep'],
                'subgroup1_within': self.group.subgroup1_within,
                'subgroup2_within': self.group.subgroup2_within,
                'subgroup1_between': self.group.subgroup1_between,
                'subgroup2_between': self.group.subgroup2_between,
                'IPD_payoff':  self.player.payoff + self.player.payoff_extra,
                'id_in_group': self.player.id_in_group,
                'role': self.player.role(),
                'payoff_extra': self.player.payoff_extra,
                'exp_right': self.player.exp_right,
                'final_payoff_with_endowment': Constants.show_up + self.player.payoff_extra +  self.player.payoff ,
                'subtract_b': self.player.subtract_b,
                'payback_a': self.player.payback_a,
                'payback_b': self.player.payback_b,

            }


class BeforeEnd( Page ):
        pass

class Results(Page):
    def vars_for_template(self):
        return {
            'final_payoff_with_endowment': Constants.show_up +  self.player.payoff +  self.player.payoff_extra,
            'id_in_group': self.player.id_in_group
        }
class MyWaitPage( WaitPage ):
    title_text = "Bitte warten Sie, bis die anderen Teilnehmer bereit sind."
    def after_all_players_arrive(self):
         self.group.set_payoffs()

page_sequence = [
    BeforeEnd,
    MyWaitPage,
    MyPage,
    Results

]



