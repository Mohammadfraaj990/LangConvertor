import requests
import os

def convert_code(code, source_lang, target_lang):
    api_key = os.getenv("OPENROUTER_API_KEY")  # or directly paste your key

    prompt = f"Convert this {source_lang} code to {target_lang}:\n\n{code}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/Mohammadfraaj990/LangConvertor",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
    result = response.json()

    return result['choices'][0]['message']['content']
