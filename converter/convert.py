import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the correct root directory
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"

def convert_code(code, source_lang, target_lang):
    try:
        if not api_key:
            return "❌ No API key found. Please check your .env file."

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        messages = [
            {"role": "system", "content": "You convert programming code between languages. Return only the code."},
            {"role": "user", "content": f"Convert this code from {source_lang} to {target_lang}:\n{code}"}
        ]

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json={"model": MODEL, "messages": messages, "max_tokens": 800}
        )

        data = response.json()
        if 'choices' in data:
            return data['choices'][0]['message']['content']
        else:
            return f"❌ Conversion failed.\n\n{data}"

    except Exception as e:
        return f"❌ Error: {e}"
