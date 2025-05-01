import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and validate it
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

openai.api_key = api_key

def generate_explanations(code):
    prompt = (
        "You are a professor teaching code to a beginner student."
        " Explain the following code line by line in an easy-to-understand way:"
        f"\n\n{code}\n\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
