import os

# 환경 변수 기반 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MAKE_API_KEY = os.getenv("MAKE_API_KEY")
FSS_API_KEY = os.getenv("FSS_API_KEY")

# API 관련 기본 설정
BASE_URL = "https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
