import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MAKE_API_KEY = os.getenv("MAKE_API_KEY")

# API 관련 기본 설정
BASE_URL = "https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"