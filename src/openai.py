from openai import OpenAI
from utils.logger import get_logger
from utils.config_loader import  get_config

config = get_config()
log = get_logger()

client = OpenAI(api_key=config['OPEN_AI_KEY'])

def ask(prompt):
    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response
    
    except Exception as e:
        log.error(f"Error while making the API call : {e}")
        raise e

prompt = "What is Data Engineering?"
response = ask(prompt= prompt)

log.info(f"LLM Response is : {response}")
