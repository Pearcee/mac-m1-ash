# settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DOMAIN = os.environ.get("DOMAIN")
print(DOMAIN)
