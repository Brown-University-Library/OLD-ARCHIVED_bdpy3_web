# -*- coding: utf-8 -*-

import json, os


API_AUTHORIZATION_CODE = os.environ['BDPY3WEB__API_AUTHORIZATION_CODE']  # for v1
API_IDENTITY = os.environ['BDPY3WEB__API_IDENTITY']  # for v1

LEGIT_IPS = json.loads( os.environ['BDPY3WEB__LEGIT_IPS'] )

README_URL = os.environ['BDPY3WEB__README_URL']

