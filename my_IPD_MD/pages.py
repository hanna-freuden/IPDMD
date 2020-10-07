from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
               }
class Intro2(Page):
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
        }

class Intro3(Page):
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
        }
class Intro4(Page):
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
        }
class Intro5(Page):
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
        }
class Intro6(Page):
    form_model = 'player'
    form_fields = ['ex_sum_a', 'ex_sum_b',  'ex_back_a', 'ex_back_b',  'ex_sum']
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
        }
    def ex_sum_a_error_message(self, value):
        print('value is', value)
        if value > 15 or value < 15:
            return 'Die richtige Antwort ist 15 €.'

    def ex_sum_b_error_message(self, value):
        print('value is', value)
        if value > 15 or value < 15:
            return 'Die richtige Antwort ist 15 €.'

    def ex_back_a_error_message(self, value):
        print( 'value is', value )
        if value > 7.5 or value < 7.5:
            return 'Die richtige Antwort ist 15*0,50=7,50 €.'

    def ex_back_b_error_message(self, value):
        print( 'value is', value )
        if value > 7.5 or value < 7.5:
            return 'Die richtige Antwort ist 15*0,50=7,50 €.'

    def ex_sum_error_message(self, value):
        print( 'value is', value )
        if value > 15 or value < 15:
            return 'Die richtige Antwort ist 7,50 + 7,50 = 15 €.'


class Intro7(Page):
    form_model = 'player'
    form_fields = ['ex_sum_a1', 'ex_sum_b1', 'ex_minus1', 'ex_minus', 'ex_final' ]
    def vars_for_template(self):
        return {
                'show_up': Constants.show_up,
        }


class Choice(Page):
    form_model = 'player'
    form_fields = ['contribution_within', 'contribution_between', 'keep']


    def error_message(self, values):
        print('values is', values)
        if values["contribution_within"] +values["contribution_between"]  +values["keep"]> 10 or values["contribution_within"] +values["contribution_between"]  +values["keep"]<10 :
            return 'Die Summe muss 10 € ergeben.'


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
            self.group.set_payoffs()



class Results(Page):
    def vars_for_template(self):
        return {
                'contribution_within': self.player.contribution_within,
                'contribution_between': self.player.contribution_between,
                'keep': self.player.keep,
             }

    def before_next_page(self):
            self.participant.vars['contribution_within'] = self.player.contribution_within
            self.participant.vars['contribution_between'] = self.player.contribution_between
            self.participant.vars['keep'] = self.player.keep


class Expectations(Page):
    form_model = 'player'
    form_fields = ['exp_own_a', 'exp_own_b', 'exp_other_a', 'exp_other_b']

    def error_message(self, values):
        print('values is', values)
        if values["exp_own_a"] + values["exp_own_b"] > 10 or values["exp_other_a"] +values["exp_other_b"] >10 :
            return 'Die Summe muss 10 € ergeben.'

    def before_next_page(self):
        self.participant.vars['exp_own_a'] = self.player.exp_own_a
        self.participant.vars['exp_own_b'] = self.player.exp_own_b
        self.participant.vars['exp_other_a'] = self.player.exp_other_a
        self.participant.vars['exp_other_b'] = self.player.exp_other_b


page_sequence = [
    Intro,
    Intro2,
    Intro3,
    Intro4,
    Intro6,
    Intro7,
    Intro5,
    Choice,
    Results,
    Expectations,
]




