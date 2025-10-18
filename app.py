import streamlit as st
import random

st.title("🍽️ GastroGuide Restaurant Bot")

# Simple restaurant logic
restaurants = {
    "italian": ["Mario's Trattoria", "Bella Napoli", "Pasta Paradise"],
    "chinese": ["Dragon Palace", "Happy Buddha", "Wok This Way"],
    "indian": ["Taj Mahal", "Curry House", "Spice Garden"]
}

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I can help you find restaurants. What cuisine?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Find restaurants..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Simple bot logic
    if "italian" in prompt.lower():
        response = f"I recommend: {', '.join(restaurants['italian'])}"
    elif "chinese" in prompt.lower():
        response = f"I recommend: {', '.join(restaurants['chinese'])}"
    elif "indian" in prompt.lower():
        response = f"I recommend: {', '.join(restaurants['indian'])}"
    elif "book" in prompt.lower():
        response = f"🎉 Table booked! Your reservation ID: GGR{random.randint(1000,9999)}"
    else:
        response = "I can help you find Italian, Chinese, or Indian restaurants!"

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})