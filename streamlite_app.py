import streamlit as st
import openai
import pyttsx3

engine = pyttsx3.init()

def generate(prompt):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message['content']
    engine.say(result)
    engine.runAndWait()
    return result

def clear():
    st.empty()

st.title("ChatBot")

# Load and display the face_img
face_img = st.image("women_wonder.gif", use_column_width=True)

prompt = st.text_input("Enter your question:")
st.write("")  # Adding some space between input and buttons

# Centering the buttons along the x-axis
col1, col2, col3 = st.columns([4, 4, 1])
with col2:
    if st.button("Generate"):
        result = generate(prompt)
        st.write(result)

with col2:
    if st.button("Clear"):
        clear()
