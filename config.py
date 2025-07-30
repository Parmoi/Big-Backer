# Handles config loading

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Values found in the .env file
    GOOGLE_PLACES_API_KEY = os.getenv('GOOGLE_PLACES_API_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False