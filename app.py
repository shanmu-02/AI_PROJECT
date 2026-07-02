import streamlit as st
import os
from google import genai

# Page configuration
st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓", layout="wide")

# Initialize Gemini Client
# It automatically picks up the GEMINI_API_KEY environment variable
try:
    client = genai.Client()
except Exception as e:
    st.error("Please set your GEMINI_API_KEY environment variable.")
    st.stop()

# --- Sidebar Configuration ---
st.sidebar.header("⚙️ AI Buddy Settings")
persona = st.sidebar.text_input(
    "1. Define AI Persona", 
    value="a patient, visual-thinking Computer Science mentor"
)
topic = st.sidebar.text_input(
    "2. Define Topic / Concept", 
    value="Binary Search"
)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by `gemini-2.5-flash` & Streamlit")

# --- Main App Interface ---
st.title("🎓 AI Learning Buddy Project")
st.write("Test your 5 reusable prompts dynamically below.")

# Create tabs for each of your 5 reusable prompts
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Explanation", 
    "2. Real-Life Example", 
    "3. Quiz Generator", 
    "4. Feedback", 
    "5. Full Session"
])

# Helper function to generate content
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

# --- TAB 1: Explanation Prompt ---
with tab1:
    st.subheader("💡 Simple Explanation")
    st.info(f"**Prompt template applied:** You are [{persona}]. Explain [{topic}] in simple language as if teaching a 15-year-old...")
    
    if st.button("Generate Explanation", key="btn_exp"):
        prompt = f"You are {persona}. Explain {topic} in simple language as if teaching a 15-year-old student. Use easy words, one clear analogy, and keep it short and engaging."
        result = generate_response(prompt)
        st.markdown(result)

# --- TAB 2: Real-Life Example Prompt ---
with tab2:
    st.subheader("🌟 Real-Life Example")
    st.info(f"**Prompt template applied:** You are [{persona}]. Give one clear real-life example of [{topic}] and explain how it works...")
    
    if st.button("Generate Real-Life Example", key="btn_ex"):
        prompt = f"You are {persona}. Give one clear real-life example of {topic} and explain how it works in simple terms."
        result = generate_response(prompt)
        st.markdown(result)

# --- TAB 3: Quiz Generator Prompt ---
with tab3:
    st.subheader("📝 Quiz Generator")
    st.info(f"**Prompt template applied:** Create 5 multiple-choice questions on [{topic}] with options (A, B, C, D) and short explanations...")
    
    if st.button("Generate Quiz Questions", key="btn_quiz"):
        prompt = f"You are {persona}. Create 5 multiple-choice questions on {topic}. Each question should have 4 options (A, B, C, D). After each question, provide the correct answer and a short explanation."
        result = generate_response(prompt)
        st.markdown(result)

# --- TAB 4: Feedback Prompt ---
with tab4:
    st.subheader("✅ Student Feedback Evaluator")
    st.info(f"**Prompt template applied:** Evaluate student's answer for a given question...")
    
    # Custom inputs for the feedback feature
    sample_question = st.text_area("Paste the Quiz Question here:", value=f"What is the time complexity of {topic} in the best case?")
    student_answer = st.text_input("Enter Student's Answer:", value="O(1)")
    
    if st.button("Evaluate Answer", key="btn_feedback"):
        prompt = f"You are {persona}. The student answered '{student_answer}' for this question: [{sample_question}]. Give encouraging feedback. If the answer is wrong, politely explain the correct answer."
        result = generate_response(prompt)
        st.markdown(result)

# --- TAB 5: Full Session Prompt (Main Tutor) ---
with tab5:
    st.subheader("🤖 Interactive Full Tutor Session")
    st.info(f"**Prompt template applied:** Initialize a warm, patient, step-by-step tutoring workflow for [{topic}]...")
    
    if st.button("Launch Tutor Session Initialization", key="btn_session"):
        prompt = f"You are {persona}, a friendly and patient tutor for {topic}. Greet the student warmly, ask about their current knowledge level, then help them learn step by step. Explain concepts clearly, give examples, ask questions, and provide feedback."
        result = generate_response(prompt)
        st.markdown(result)