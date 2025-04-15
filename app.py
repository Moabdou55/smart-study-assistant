import streamlit as st
from transformers import pipeline

# Load summarizer pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

# Flashcard-style Q&A (mocked for simplicity)
def generate_flashcards(text):
    return [
        {"Q": "What is the main idea?", "A": text.split(".")[0]},
        {"Q": "What important fact is mentioned?", "A": text.split(".")[-2]},
        {"Q": "What is this text about?", "A": text.split(".")[0]},
    ]

# Quiz questions (mocked)
def generate_quiz(text):
    return [
        "1. What is the main purpose of this topic?",
        "2. What does the text explain or describe?",
        "3. Why is this concept important?"
    ]

# Streamlit UI
st.title("📚 Smart Study Assistant")
st.write("""
Paste your academic text below. The assistant will:
- Generate a **summary**
- Create simple **flashcards** (Q&A)
- Offer **quiz-style questions**
""")

user_input = st.text_area("📝 Enter your study text here:", height=200)

if st.button("🚀 Generate Study Material") and user_input:
    with st.spinner("Analyzing your text..."):
        summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        flashcards = generate_flashcards(user_input)
        quiz = generate_quiz(user_input)

    st.subheader("📌 Summary")
    st.success(summary)

    st.subheader("📇 Flashcards")
    for card in flashcards:
        st.write(f"**Q:** {card['Q']}")
        st.write(f"**A:** {card['A']}")
        st.markdown("---")

    st.subheader("❓ Quiz Questions")
    for q in quiz:
        st.write(q)
