import requests

api_key = "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"  # ⬅ Replace with your actual key
MODEL = "mistralai/mistral-7b-instruct"  # Free model

def convert_code(code, source_lang, target_lang):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        messages = [
            {"role": "system", "content": "You convert programming code between languages."},
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
            return f"Conversion failed.\n\n{data}"

    except Exception as e:
        return f"Error: {e}"
