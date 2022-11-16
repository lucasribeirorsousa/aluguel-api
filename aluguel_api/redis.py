import redis as r

from .settings import REDIS_HOST, REDIS_PORT, REDIS_DB

redis = r.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)