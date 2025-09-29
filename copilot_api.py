import requests
import os

def get_copilot_fix(code_snippet, api_url=None, api_key=None):
    """
    Send code_snippet to Copilot/LLM API and return suggested fix.
    Replace api_url and api_key with your provider's endpoint and credentials.
    """
    api_url = api_url or os.getenv('COPILOT_API_URL')
    api_key = api_key or os.getenv('COPILOT_API_KEY')
    if not api_url or not api_key:
        raise ValueError("Copilot API URL and key must be set.")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"prompt": code_snippet, "max_tokens": 512}
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("choices", [{}])[0].get("text", "")
