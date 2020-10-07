from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Hanna Freudenreich'

doc = """
Calculates results of my_IDP_MD
"""


class Constants(BaseConstants):
    name_in_url = 'my_IPD_MD_results'
    players_per_group = 6
    num_rounds = 1
    endowment = c(10)
    multiplier = 0.5
    show_up = c(15)


class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    exp_own_a_right = models.IntegerField( initial=0 )
    exp_own_b_right = models.IntegerField( initial=0 )
    exp_other_a_right = models.IntegerField( initial=0 )
    exp_other_b_right = models.IntegerField( initial=0 )
    exp_right = models.IntegerField( initial=0 )
    payoff_extra = models.CurrencyField( initial=0 )
    payback_a = models.CurrencyField( initial=0 )
    payback_b = models.CurrencyField( initial=0 )
    subtract_b = models.CurrencyField( initial=0 )
    final_payoff_with_endowment = models.CurrencyField( initial=0 )

    def role(self):
        if self.id_in_group <= 3:
            return 'subgroup1'
        else:
            return 'subgroup2'

    def set_final(self):
            self.role=self.participant.vars['role']
            self.final_payoff_with_endowment =self.player.payoff + Constants.show_up
            self.participant.vars['final_payoff_with_endowment'] = self.final_payoff_with_endowment
            self.participant.vars['exp_right'] = self.player.exp_right
            self.participant.vars['payoff_extra'] = Constants.multiplier * (self.player.exp_right)

class Group( BaseGroup ):
    #contributions
    subgroup1_within = models.CurrencyField( initial=0 )
    subgroup1_between = models.CurrencyField( initial=0 )
    subgroup2_within = models.CurrencyField( initial=0 )
    subgroup2_between = models.CurrencyField( initial=0 )
    #expectations about contributions
    avg_subgroup1_within = models.CurrencyField( initial=0 )
    avg_subgroup1_between = models.CurrencyField( initial=0 )
    avg_subgroup2_within = models.CurrencyField( initial=0 )
    avg_subgroup2_between = models.CurrencyField( initial=0 )


    def set_payoffs(self):

        for p in self.get_players():
            if p.role() == 'subgroup1':
                self.subgroup1_within += p.participant.vars['contribution_within']
                self.avg_subgroup1_within =  (self.subgroup1_within - p.participant.vars['contribution_within']) / 2
                self.subgroup1_between += p.participant.vars['contribution_between']
                self.avg_subgroup1_between =  (self.subgroup1_between - p.participant.vars['contribution_between']) / 2

            elif p.role() == 'subgroup2':
                self.subgroup2_within += p.participant.vars['contribution_within']
                self.avg_subgroup2_within = (self.subgroup2_within - p.participant.vars['contribution_within']) / 2
                self.subgroup2_between += p.participant.vars['contribution_between']
                self.avg_subgroup2_between = (self.subgroup2_between - p.participant.vars['contribution_between']) / 2

# determine whether expectations were correct
        for p in self.get_players():
            if p.role() == 'subgroup1':
                if p.participant.vars['exp_own_a'] == round( self.avg_subgroup1_within ): p.exp_own_a_right = 1
                if p.participant.vars['exp_own_b'] == round( self.avg_subgroup1_between ):  p.exp_own_b_right = 1
                if p.participant.vars['exp_other_a'] == round( self.avg_subgroup2_within ): p.exp_other_a_right = 1
                if p.participant.vars['exp_other_b'] == round( self.avg_subgroup2_between ):  p.exp_other_b_right = 1
            elif p.role() == 'subgroup2':
                if p.participant.vars['exp_own_a'] == round( self.avg_subgroup2_within ): p.exp_own_a_right = 1
                if p.participant.vars['exp_own_b'] == round( self.avg_subgroup2_between ):  p.exp_own_b_right = 1
                if p.participant.vars['exp_other_a'] == round( self.avg_subgroup1_within ): p.exp_other_a_right = 1
                if p.participant.vars['exp_other_b'] == round( self.avg_subgroup1_between ):  p.exp_other_b_right = 1

#final payoffs
        for p in self.get_players():
            if p.role() == 'subgroup1':
              p.exp_right = p.exp_own_a_right +p.exp_own_b_right +p.exp_other_a_right +p.exp_other_a_right
              p.payoff_extra = (p.exp_own_a_right + p.exp_own_b_right + p.exp_other_a_right + p.exp_other_a_right) * 0.5
              p.payback_a = Constants.multiplier * self.subgroup1_within
              p.payback_b = Constants.multiplier * self.subgroup1_between
              p.subtract_b = - Constants.multiplier * self.subgroup2_between
              p.payoff = Constants.endowment -p.participant.vars['contribution_between'] - p.participant.vars['contribution_within'] + p.payback_b + p.payback_a +p.subtract_b +  p.payoff_extra
              p.final_payoff_with_endowment = Constants.show_up + p.payoff
            elif p.role() == 'subgroup2':
              p.exp_right = p.exp_own_a_right + p.exp_own_b_right + p.exp_other_a_right + p.exp_other_a_right
              p.payoff_extra = (p.exp_own_a_right + p.exp_own_b_right + p.exp_other_a_right + p.exp_other_a_right) * 0.5
              p.payback_a = Constants.multiplier * self.subgroup2_within
              p.payback_b = Constants.multiplier * self.subgroup2_between
              p.subtract_b = - Constants.multiplier * self.subgroup1_between
              p.payoff = Constants.endowment- p.participant.vars['contribution_between'] - p.participant.vars['contribution_within'] + p.payback_b + p.payback_a + p.subtract_b +  p.payoff_extra
              p.final_payoff_with_endowment = Constants.show_up +  p.payoff


