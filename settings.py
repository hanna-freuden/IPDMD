
import os
from os import environ


import dj_database_url

import otree.settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 15,
    'doc': "",
}


SESSION_CONFIGS = [
    {
        'name': 'my_IPD_MD',
        'display_name': "Intergroup Prisoner's Dilemma Maximizing Differences Game (German)",
        'num_demo_participants': 6,
        'app_sequence': ['my_IPD_MD','my_IPD_MD_results']
    },

]

LANGUAGE_CODE = 'de'


REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


OTREE_PRODUCTION=1

if environ.get('OTREE_PRODUCTION') not in {'None', '', '1'}:
     DEBUG = False
else:
    DEBUG = True
# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '1'})

DEMO_PAGE_INTRO_HTML = """
This is an oTree-implementation of the Intergroup Prisoner's Dilemma Maximizing Differences (IPDMD) game based on the paper by Halevy et al. (2008) in Psychological Science. 
"""


INSTALLED_APPS = []
EXTENSION_APPS = []
SECRET_KEY=''

otree.settings.augment_settings(globals())
