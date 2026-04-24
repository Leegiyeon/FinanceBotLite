# FinanceBotLite

FinanceBotLite는 **금융 추천 + 미니미 커스터마이징 + 간단한 인앱 경제**를 결합한 Streamlit MVP 앱입니다.
기존의 단순 질문형 추천 앱에서 확장되어, 사용자가 반복 방문하며 금융 습관을 만들 수 있는 구조를 목표로 합니다.

## 현재 구현 상태 (2026-04-24 기준)

### ✅ 구현 완료
- 탭형 UI: `홈 / 미니룸 / 샵 / 프로필`
- 맞춤 추천 입력: 목적, 월 예산, 위험 성향, 자유 질문
- 추천 결과 카드 + 주의사항 표시
- 추천 조회 보상(+코인)
- 미니미 커스터마이징(헤어/의상/배경 장착)
- 샵 구매 로직(코인 사용)
- PRO 구독 데모 토글
- 파스텔 톤 귀여운 테마 CSS 적용
- 외부 API 실패 시 샘플 데이터 fallback

### 🚧 다음 단계
- 실제 결제 연동(스토어/IAP 또는 웹 결제)
- 아이템 확장 및 시즌 테마팩
- 이벤트 로깅/대시보드
- 온보딩/리텐션 실험(A/B)

---

## 기술 스택
- Python 3.10+
- Streamlit
- 표준 라이브러리 기반 API 요청(`urllib`)

---

## 설치 및 실행

## 1) 의존성 설치
```bash
pip install -r requirements.txt
```

## 2) 앱 실행
```bash
streamlit run app.py
```

## 3) 테스트 실행
```bash
pytest -q
```

---

## 환경 변수
현재 코드는 키가 없어도 fallback 데이터로 동작합니다. 실제 연동 시 아래를 설정하세요.

- `OPENAI_API_KEY` (향후 실제 분석 연동용)
- `FSS_API_KEY` (금융감독원 API)
- `MAKE_API_KEY` (현재 코드에서 사용하지 않음, 향후 확장용)

예시:
```bash
export OPENAI_API_KEY="..."
export FSS_API_KEY="..."
export MAKE_API_KEY="..."
```

---

## 디자인 파일 가이드
디자인은 CSS 파일 하나로 관리합니다.

- 메인 스타일: `assets/styles.css`
- 로딩 위치: `app.py`의 `load_css("assets/styles.css")`

즉, 컬러/버튼/탭/배경 스타일을 바꾸려면 `assets/styles.css`만 수정하면 됩니다.

---

## 프로젝트 구조
```text
FinanceBotLite/
├── app.py
├── config.py
├── requirements.txt
├── pytest.ini
├── README.md
├── assets/
│   └── styles.css
├── docs/
│   ├── REBOOT_EXECUTION_PLAN.md
│   └── WORK_TODO.md
├── tests/
│   ├── test_api_handler.py
│   └── test_test_processing.py
└── utils/
    ├── __init__.py
    ├── api_handler.py
    └── text_processing.py
```

---

## 면책 고지
본 앱의 추천 결과는 참고용 정보이며, 투자 권유가 아닙니다.
상품 가입 전 약관/설명서/수수료/중도해지 조건을 반드시 확인하세요.
