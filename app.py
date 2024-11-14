import streamlit as st
from utils.api_handler import fetch_financial_products
from utils.text_processing import analyze_question

st.title("FinanceBotLite")
st.write("간단한 질문을 입력하여 최적의 금융 상품을 추천받아 보세요.")

# 사용자 입력
user_question = st.text_input("금융 상품에 대해 알고 싶은 내용을 입력하세요:")

if st.button("추천받기") and user_question:
    # 질문 분석 및 추천 호출
    analysis_result = analyze_question(user_question)
    recommendations = fetch_financial_products(analysis_result)

    # 결과 출력
    st.subheader("추천 금융 상품")
    for product in recommendations:
        st.write(f"**{product['name']}**")
        st.write(product['description'])
        st.write("---")
