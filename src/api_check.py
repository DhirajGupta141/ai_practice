from openai import OpenAI
from utils.logger import get_logger
from utils.config_loader import  get_config

config = get_config()
log = get_logger()

client = OpenAI(api_key=config['OPEN_AI_KEY'])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello Gen AI World!"}]
)

log.info(response.choices[0].message["content"])
