import streamlit as st
import os
from google import genai

# Page configuration
st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓", layout="centered")

# Initialize Gemini Client
try:
    client = genai.Client()
except Exception as e:
    st.error("Please set your GEMINI_API_KEY environment variable.")
    st.stop()

# --- Main App Interface ---
st.title("🎓 AI Learning Buddy Manasvi")  # <-- put your buddy's name here

topic = st.text_input("Enter a Topic")

activity = st.selectbox(
    "Choose Activity",
    ["Explain Concept", "Real-Life Example", "Quiz Generator", "Feedback", "Full Tutor Session", "Ask Anything"]
)

persona = "a patient, visual-thinking Computer Science mentor"

def generate_response(prompt_text):
    with st.spinner("AI Buddy is thinking..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt_text,
            )
            return response.text
        except Exception as e:
            return f"Error calling Gemini API: {e}"

def build_prompt(topic, activity, persona):
    if activity == "Explain Concept":
        return f"You are {persona}. Explain {topic} in simple language as if teaching a 15-year-old student. Use easy words, one clear analogy, and keep it short and engaging."
    elif activity == "Real-Life Example":
        return f"You are {persona}. Give one clear real-life example of {topic} and explain how it works in simple terms."
    elif activity == "Quiz Generator":
        return f"You are {persona}. Create 5 multiple-choice questions on {topic}. Each question should have 4 options (A, B, C, D). After each question, provide the correct answer and a short explanation."
    elif activity == "Feedback":
        return f"You are {persona}. Give general encouraging feedback and common mistakes students make when learning {topic}."
    elif activity == "Full Tutor Session":
        return f"You are {persona}, a friendly and patient tutor for {topic}. Greet the student warmly, ask about their current knowledge level, then help them learn step by step."
    else:  # Ask Anything
        return f"You are {persona}. Answer this question about {topic} in a clear, simple, and friendly way."

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        prompt = build_prompt(topic, activity, persona)
        result = generate_response(prompt)
        st.markdown(result)
