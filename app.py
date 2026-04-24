import streamlit as st
from utils.api_handler import fetch_financial_products
from utils.text_processing import analyze_question


st.set_page_config(page_title="FinanceBotLite", page_icon="💸", layout="centered")


def load_css(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


def init_state():
    defaults = {
        "coins": 120,
        "owned_items": {"basic_hair", "basic_top", "basic_bg"},
        "equipped": {
            "hair": "basic_hair",
            "top": "basic_top",
            "bg": "basic_bg",
        },
        "pro_user": False,
        "streak": 1,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_avatar():
    hair_label = ITEM_LABELS[st.session_state["equipped"]["hair"]]
    top_label = ITEM_LABELS[st.session_state["equipped"]["top"]]
    bg_label = ITEM_LABELS[st.session_state["equipped"]["bg"]]
    st.markdown(
        f"""
### 🧸 나의 미니미
- 헤어: **{hair_label}**
- 의상: **{top_label}**
- 배경: **{bg_label}**
"""
    )


ITEMS = [
    {"id": "basic_hair", "slot": "hair", "name": "기본 단발", "price": 0},
    {"id": "ribbon_hair", "slot": "hair", "name": "리본 헤어", "price": 80},
    {"id": "basic_top", "slot": "top", "name": "기본 후드", "price": 0},
    {"id": "mint_top", "slot": "top", "name": "민트 니트", "price": 110},
    {"id": "basic_bg", "slot": "bg", "name": "기본 방", "price": 0},
    {"id": "sky_bg", "slot": "bg", "name": "파스텔 하늘 방", "price": 160},
]
ITEM_LABELS = {item["id"]: item["name"] for item in ITEMS}


init_state()
load_css("assets/styles.css")
st.title("FinanceBotLite")
st.caption("금융 추천도 받고, 내 미니미도 꾸미는 금융 라이프 앱")

home_tab, room_tab, shop_tab, profile_tab = st.tabs(["홈", "미니룸", "샵", "프로필"])

with home_tab:
    st.subheader("맞춤 추천")
    purpose = st.selectbox("목적", ["비상금", "저축", "단기목표", "안정형 투자"])
    monthly_budget = st.slider("월 납입 가능 금액(만원)", 5, 300, 50)
    risk = st.radio("위험 성향", ["낮음", "중간", "높음"], horizontal=True)
    user_question = st.text_input("궁금한 금융 질문")

    if st.button("추천받기"):
        analysis_input = (
            f"목적: {purpose}, 월예산: {monthly_budget}만원, 위험성향: {risk}, 질문: {user_question}"
        )
        analysis_result = analyze_question(analysis_input)
        recommendations = fetch_financial_products()

        st.success("추천이 생성되었습니다.")
        st.write(f"분석 요약: {analysis_result}")
        st.markdown("#### 추천 금융 상품")

        for idx, product in enumerate(recommendations[:3], start=1):
            name = product.get("fin_prdt_nm") or product.get("name") or "이름 없음"
            company = product.get("kor_co_nm") or "제공기관 정보 없음"
            note = product.get("etc_note") or product.get("description") or "설명 정보 없음"
            st.markdown(f"**{idx}. {name}**")
            st.write(f"- 기관: {company}")
            st.write(f"- 추천 이유: {note}")
            st.write("- 주의사항: 가입 전 금리/수수료/중도해지 조건 확인")
            st.write("---")

        st.session_state["coins"] += 15
        st.info("추천 확인 보상 +15 코인 🎉")

with room_tab:
    st.subheader("미니룸 커스터마이징")
    render_avatar()

    owned_by_slot = {"hair": [], "top": [], "bg": []}
    for item in ITEMS:
        if item["id"] in st.session_state["owned_items"]:
            owned_by_slot[item["slot"]].append(item)

    for slot_key, slot_name in [("hair", "헤어"), ("top", "의상"), ("bg", "배경")]:
        options = owned_by_slot[slot_key]
        if not options:
            st.write(f"{slot_name} 아이템이 없습니다.")
            continue
        labels = [item["name"] for item in options]
        current_item = st.session_state["equipped"][slot_key]
        current_label = ITEM_LABELS[current_item]
        selected_label = st.selectbox(
            f"{slot_name} 장착", labels, index=labels.index(current_label), key=f"equip_{slot_key}"
        )
        selected_item = next(item for item in options if item["name"] == selected_label)
        st.session_state["equipped"][slot_key] = selected_item["id"]

with shop_tab:
    st.subheader("아이템 샵")
    st.write(f"보유 코인: **{st.session_state['coins']}**")
    st.write("기본 아이템 외 상품을 구매해 미니룸을 꾸며보세요.")

    for item in ITEMS:
        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            st.write(f"{item['name']} ({item['slot']})")
        with col2:
            st.write("무료" if item["price"] == 0 else f"{item['price']} 코인")
        with col3:
            owned = item["id"] in st.session_state["owned_items"]
            if owned:
                st.caption("보유 중")
            else:
                if st.button(f"구매-{item['id']}"):
                    if st.session_state["coins"] >= item["price"]:
                        st.session_state["coins"] -= item["price"]
                        st.session_state["owned_items"].add(item["id"])
                        st.success(f"{item['name']} 구매 완료")
                    else:
                        st.warning("코인이 부족합니다.")

    st.markdown("---")
    st.markdown("### PRO 구독")
    st.write("PRO에서는 프리미엄 테마와 고급 추천 리포트를 사용할 수 있습니다.")
    if st.session_state["pro_user"]:
        st.success("현재 PRO 구독 상태입니다.")
    else:
        if st.button("월 구독 시작(데모)"):
            st.session_state["pro_user"] = True
            st.success("PRO 구독이 활성화되었습니다. (데모)")

with profile_tab:
    st.subheader("내 프로필")
    render_avatar()
    st.write(f"연속 방문: {st.session_state['streak']}일")
    st.write(f"보유 코인: {st.session_state['coins']}")
    st.write(f"PRO 여부: {'예' if st.session_state['pro_user'] else '아니오'}")
    st.caption("투자 권유가 아닌 참고용 정보입니다. 가입 전 상품 설명서를 확인하세요.")
