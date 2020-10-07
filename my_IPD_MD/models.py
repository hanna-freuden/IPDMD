from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Bot,
    Currency as c, currency_range
)


author = 'Hanna Freudenreich'

doc = """
An implementation of the intergroup prisoners' dilemma maximizing difference game (IPD-MD) (Halevy et al. 2008) for oTree (in German).
From Halevy et al. (2008): "The game involves two groups. Each group member is given a monetary endowment and can decide how much of it to contribute. Contribution can be made to either of two pools, one that benefits the ingroup at a personal cost and another that, in addition, harms the out-group"
"""
class Constants(BaseConstants):
    name_in_url = 'my_IPDMD'
    players_per_group = 6
    num_rounds = 1
    endowment = c(10)
    show_up = c(15)
    multiplier = 0.5



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    def role(self):
        if self.id_in_group <= 3:
            return 'subgroup1'
        else:
            return 'subgroup2'
  
class Player(BasePlayer):
#contributions
    contribution_within = models.CurrencyField(min=0, max=Constants.endowment, label="")
    contribution_between = models.CurrencyField(min=0, max=Constants.endowment, label="")
    keep = models.CurrencyField( min=0, max=Constants.endowment , label="")

#examples and tests of understanding
    ex_sum_a = models.CurrencyField(min=0, max=50, label="")
    ex_sum_b = models.CurrencyField(min=0, max=50, label="")
    ex_back_a = models.CurrencyField(min=0, max=50, label="")
    ex_back_b = models.CurrencyField(min=0, max=50, label="")
    ex_back_a1 = models.CurrencyField(min=0, max=50, label="")
    ex_back_b1 = models.CurrencyField(min=0, max=50, label="")
    ex_sum = models.CurrencyField(min=0, max=50, label="")
    ex_sum_a1 = models.CurrencyField(min=0, max=50, label="")
    ex_sum_b1 = models.CurrencyField(min=0, max=50, label="")
    ex_minus = models.CurrencyField(min=0, max=50, label="")
    ex_final = models.CurrencyField( min=0, max=50, label="" )
    ex_minus1 = models.CurrencyField( min=0, max=50, label= "")

#expectations about other group members' contributions
    exp_own_a = models.CurrencyField(min=0, max=Constants.endowment, label='') #label="Was denken Sie: wieviel hat jedes Mitglied Ihrer Gruppe im Durchschnitt in Topf A eingezahlt?")
    exp_own_b = models.CurrencyField(min=0, max=Constants.endowment, label='') #label="Was denken Sie: wieviel hat jedes Mitglied Ihrer Gruppe im Durchschnitt in Topf B eingezahlt?")
    exp_other_a = models.CurrencyField( min=0, max=Constants.endowment, label='')#label="Was denken Sie: wieviel hat jedes Mitglied der anderen Gruppe im Durchschnitt in Topf A eingezahlt?" )
    exp_other_b = models.CurrencyField( min=0, max=Constants.endowment, label='')#label="Was denken Sie: wieviel hat jedes Mitglied der anderen Gruppe im Durchschnitt in Topf B eingezahlt?" )

