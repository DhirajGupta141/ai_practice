
import os 
from dotenv import load_dotenv 
from utils.logger import get_logger

log = get_logger()

load_dotenv()  # loads the .env data in the os

def get_config():
    log.info(f"Config File is Loaded")
    return {
        'OPEN_AI_KEY' : os.getenv('OPEN_AI_KEY'),
        'GEMINI_API_KEY' : os.getenv('GEMINI_API_KEY')
    }















