import requests
from config import MAKE_API_KEY, BASE_URL, OPENAI_API_KEY
import openai

def fetch_financial_products(analysis_result):
    headers = {
        "Authorization": f"Bearer {MAKE_API_KEY}"
    }
    params = {
        "query": analysis_result
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json().get("products", [])
    else:
        return []

def get_openai_analysis(question):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=100
    )
    return response.choices[0].text.strip()