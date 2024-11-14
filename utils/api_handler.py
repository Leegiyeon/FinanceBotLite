import requests
from config import FSS_API_KEY, BASE_URL, OPENAI_API_KEY
import openai

def fetch_financial_products():
    """
    금융감독원 API에서 금융 상품 정보를 가져옵니다.
    """
    params = {
        "auth": FSS_API_KEY,     # 금융감독원 API 키
        "topFinGrpNo": "020000",  # 예금 상품 코드 (필요에 따라 변경 가능)
        "pageNo": "1"             # 페이지 번호
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json().get("result", {}).get("baseList", [])
    else:
        response.raise_for_status()

def get_openai_analysis(question):
    """
    최신 OpenAI API를 사용하여 질문을 분석하고, 답변을 생성합니다.
    """
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message['content'].strip()
