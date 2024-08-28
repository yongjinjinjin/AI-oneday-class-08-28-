from openai import OpenAI
import streamlit as st
import streamlit as st
import time

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
  with st.spinner('생성 중입니다.'):
    client = OpenAI(api_key=st.secrets["API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": keyword + "라는 제품 홍보 카피를 150자 이내로 작성해줘",
        }],
        model="gpt-4o",
    )

    chat_result = chat_completion.choices[0].message.content
    st.write(chat_result)

    client = OpenAI(api_key=st.secrets["API_KEY"])

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    st.image(image_url)
