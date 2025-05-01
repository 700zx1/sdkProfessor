import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_explanations(code):
    prompt = (
        "You are a professor teaching code to a beginner student."
        " Explain the following Python code line by line in an easy-to-understand way:"
        f"\n\n{code}\n\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
