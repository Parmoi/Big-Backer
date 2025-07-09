# Handles config loading

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_PLACES_API_KEY = os.getenv('GOOGLE_PLACES_API_KEY')