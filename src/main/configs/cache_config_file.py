import os
from dotenv import load_dotenv

# Load enviroment variables
load_dotenv()
cache_config = {
    "CACHE_TYPE": os.getenv("CACHE_TYPE"),
    "CACHE_DEFAULT_TIMEOUT": int(os.getenv("CACHE_DEFAULT_TIMEOUT")),
}
