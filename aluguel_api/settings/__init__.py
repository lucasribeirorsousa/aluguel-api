# flake8: noqa
import os
from .base import *

from dotenv import load_dotenv
load_dotenv()

env = os.getenv('ALUGUEL_ENVIRONMENT')

if env == 'PRODUCTION':
    print(f'--- {env} ENVIRONMENT ---')
    from .production import *
elif env == 'DEVELOPMENT':
    print(f'--- {env} ENVIRONMENT ---')
    from .development import *
elif env == 'HOMOLOGATION':
    print(f'--- {env} ENVIRONMENT ---')
    from .homologation import *
else:
    print(f"--- {env} ENVIRONMENT ---")
