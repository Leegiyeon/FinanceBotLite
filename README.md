# FinanceBotLite

FinanceBotLite는 간단하고 사용하기 쉬운 금융 상품 추천 서비스입니다. 사용자가 입력한 질문을 기반으로 최적의 금융 상품을 추천하여 투자 또는 금융 관련 결정을 돕습니다. OpenAI의 언어 모델과 외부 금융 데이터 API를 활용하여 사용자에게 맞춤형 추천을 제공합니다.

## 서비스 개요

- **목표**: 사용자가 간단한 질문만으로도 맞춤형 금융 상품을 추천받을 수 있도록 하는 것입니다.
- **주요 기능**:
  - 사용자 질문을 바탕으로 금융 상품 추천
  - 각 상품에 대한 간단한 설명 제공
  - Streamlit을 통해 간편한 웹 인터페이스 제공

## 기능 설명

1. **질문 입력**: 사용자가 원하는 금융 상품에 관한 질문을 입력합니다.
2. **질문 분석**: OpenAI API를 활용하여 질문의 의도를 분석하고, 상품 검색 조건을 설정합니다.
3. **상품 추천**: Make.com을 통해 외부 금융 데이터 API와 연동하여 조건에 맞는 금융 상품을 추천합니다.
4. **결과 출력**: 추천된 금융 상품과 간단한 설명을 Streamlit 인터페이스에 표시합니다.

## 기술 스택

- **프로그래밍 언어**: Python
- **프레임워크**: Streamlit
- **AI 모델**: OpenAI GPT 모델
- **API 연동**: Make.com을 통한 외부 금융 데이터 API 호출
- **배포**: Streamlit 웹 애플리케이션

## 설치 및 실행 방법

### 사전 요구사항
- Python 3.x
- OpenAI API 키
- Make.com API 계정


## 프로젝트 구조
```
FinanceBotLite/
├── app.py                     # Streamlit 메인 애플리케이션 파일
├── requirements.txt           # 필요한 Python 패키지 목록
├── README.md                  # 프로젝트 개요와 설치 방법 등을 설명하는 파일
├── config.py                  # API 키 및 기타 설정을 관리하는 파일
├── .env                       # 환경 변수 파일 (API 키 등을 여기에 저장, .gitignore에 포함)
├── utils/
│   ├── api_handler.py         # Make.com 및 OpenAI API 호출을 위한 모듈
│   ├── text_processing.py     # 질문 분석 및 텍스트 처리 기능 모듈
│   └── data_formatter.py      # 외부 API에서 가져온 데이터를 포맷팅하는 모듈
├── templates/                 # 사용자에게 보여질 템플릿 관련 파일
│   └── response_template.py   # 추천 결과의 UI 구성을 위한 템플릿
├── assets/                    # 이미지, CSS, JavaScript 등 정적 파일
├── tests/                     # 테스트 코드 파일
│   ├── test_api_handler.py    # API 호출 모듈의 테스트
│   ├── test_text_processing.py # 텍스트 처리 모듈의 테스트
│   └── test_data_formatter.py  # 데이터 포맷팅 모듈의 테스트
├── docs/                      # 프로젝트 문서
│   ├── SERVICE_PLAN.md        # 서비스 기획서
│   ├── REQUIREMENTS.md        # 요구사항 명세서
│   ├── FUNCTIONAL_SPEC.md     # 기능 명세서
│   ├── USE_CASE.md            # USE CASE 문서
│   └── UI_DESIGN.md           # UI 설계서
└── LICENSE                    # 라이센스 파일

```