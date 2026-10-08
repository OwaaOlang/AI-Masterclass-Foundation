import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads variables

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)  # prints the key value at runtime