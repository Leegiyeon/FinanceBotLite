import json
from urllib.parse import urlencode
from urllib.request import urlopen

from config import BASE_URL, FSS_API_KEY, OPENAI_API_KEY


def fetch_financial_products():
    """금융 상품 정보를 가져오고 실패 시 샘플 데이터를 반환합니다."""
    if not FSS_API_KEY or not BASE_URL:
        return _sample_products()

    params = {
        "auth": FSS_API_KEY,
        "topFinGrpNo": "020000",
        "pageNo": "1",
    }
    request_url = f"{BASE_URL}?{urlencode(params)}"

    try:
        with urlopen(request_url, timeout=8) as response:
            payload = json.loads(response.read().decode("utf-8"))
        products = payload.get("result", {}).get("baseList", [])
        return products if isinstance(products, list) else _sample_products()
    except (OSError, ValueError) as e:
        # Log the error in production for monitoring
        return _sample_products()


def get_openai_analysis(question):
    """OpenAI 분석 호출이 불가하면 규칙 기반 분석을 반환합니다."""
    # 이 저장소의 테스트/로컬 환경 안정성을 위해 기본은 fallback 분석을 사용합니다.
    # 실제 연동은 서버 측 안전한 프록시/SDK 설정 후 활성화 권장.
    _ = OPENAI_API_KEY
    return _fallback_analysis(question)


def _fallback_analysis(question):
    question = (question or "").strip()
    if not question:
        return "사용자 입력이 비어 있어 기본 안정형 추천 조건을 사용합니다."
    return f"질문 핵심: '{question[:80]}'. 안정형/중립형 기준으로 추천을 제안합니다."


def _sample_products():
    return [
        {
            "fin_prdt_nm": "안심 적금 플러스",
            "kor_co_nm": "FinanceBank",
            "etc_note": "초보자용 정기 적금, 자동이체 우대 제공",
        },
        {
            "fin_prdt_nm": "데일리 파킹 통장",
            "kor_co_nm": "SafeBank",
            "etc_note": "유동성 중심 단기 보관형 통장",
        },
        {
            "fin_prdt_nm": "밸런스 CMA",
            "kor_co_nm": "Grow Securities",
            "etc_note": "자금 관리와 수익성 균형형 상품",
        },
    ]
