#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import(
    HumanMessage,
    SystemMessage
)
import streamlit as st

chat_model = ChatOpenAI(model_name="gpt-3.5-turbo",temperature = 1)

st.title("<<독일어 번역기>>")
st.title("나는 _:blue[Herr. 챗]_ :sunglasses:")
st.title("뭐든지 번역해줄게")
st.title("")

context = """
너는 지금부터 한국에서 일하는 독일인 선생님이야. 한국어로 된 문장을 받으면 너는 그것을 독일어로 정확한 문법과 표현을 활용하여 번역해야 해. 답변은 번역한 독일어 문장으로만 해 줘.
"""

content = st.text_input('인공지능 Herr. 챗이 한국어 문장을 번역합니다!')

if st.button('번역하기'):
    with st.spinner("사전을 넘기는 중..."):
        message = [SystemMessage(content=context), HumanMessage(content=content)]

        result = chat_model.invoke(message).content
        st.write("번역한 문장은...", result)