from src.main.configs.cache_config_file import cache_config
from flask_caching import Cache

cache = Cache(config=cache_config)
