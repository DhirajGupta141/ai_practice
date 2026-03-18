
import os 
from dotenv import load_dotenv 
from logger import get_logger

log = get_logger()

load_dotenv()

def get_config():
    log.info(f"Config File is Loaded")
    return {
        'OPEN_AI_KEY' : os.getenv('OPEN_AI_KEY')
    }















