import warnings
warnings.filterwarnings(action='ignore')

from utils.logger import get_logger
from utils.config_loader import  get_config


config = get_config()
log = get_logger()


import google.generativeai as genai

genai.configure(api_key=config["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash-native-audio-latest")

def gemini_pract():
    try:
        response = model.generate_content(
            "Explain Apache Spark architecture in simple terms"
        )

        log.info(response.text)
        
    except Exception as e:
        log.error(f"Error while invoking the gemini api key : {e}")
        raise e

gemini_pract()





