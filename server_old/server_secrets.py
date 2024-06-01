import os

from dotenv import load_dotenv

load_dotenv()

REMOVEBG_API_KEY = os.getenv("REMOVEBG_API_KEY")
GOOEY_API_KEY = os.getenv("GOOEY_API_KEY")
