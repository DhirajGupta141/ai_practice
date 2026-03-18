import warnings
warnings.filterwarnings(action='ignore')

from utils.logger import get_logger
from utils.config_loader import  get_config


config = get_config()
log = get_logger()

from google import genai
from google.genai import types

client = genai.Client(api_key=config['GEMINI_API_KEY'])

# It's often cleaner to separate the config
config = types.GenerateContentConfig(
    system_instruction="You are a helpful Data Engineering expert.Always provide highly detailed, comprehensive, and long-form explanations. " \
    "Aim for exhaustive technical depth in every response.",
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    max_output_tokens=2048,
)
# get the model list available in the perticular API 
# models = client.models.list()
# for m in models:
#     log.info(m.name)

def ask(prompt):
    try:
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config
        )
        
        return response.text
    
    except Exception as e:
        log.error(f"Error while invoking the gemini api key : {e}")
        raise e

while True:
    user_question = input("Your question?: ").strip()
    
    if len(user_question) <= 5:
        log.info("Ask question with at least 5 character length")
        continue  # This prevents the API from being called with a tiny prompt

    llm_response = ask(user_question)
    log.info(llm_response)









