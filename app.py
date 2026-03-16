import streamlit as st
from chatbot import chat_with_jarvis
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Jarvis AI", page_icon="🤖")

st.title("🤖 Jarvis AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask Jarvis anything...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # convert to langchain format
    history = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            history.append(HumanMessage(content=m["content"]))
        else:
            history.append(AIMessage(content=m["content"]))

    response = chat_with_jarvis(history)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)