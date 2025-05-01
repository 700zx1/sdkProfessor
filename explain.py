import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and validate it
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

# Initialize OpenAI client with proper configuration
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1"
)

def generate_explanations(code):
    try:
        # Create a chat completion using the new client interface
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professor teaching code to a beginner student."},
                {"role": "user", "content": f"Explain the following code line by line in an easy-to-understand way:\n\n{code}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating explanation: {str(e)}"
