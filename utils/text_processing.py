from utils.api_handler import get_openai_analysis

def analyze_question(question):
    """
    OpenAI API를 사용하여 질문의 의도를 분석하고, 추천을 위한 조건을 생성합니다.
    """
    return get_openai_analysis(question)