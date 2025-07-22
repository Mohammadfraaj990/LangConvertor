import streamlit as st
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Ensure root folder is in path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from converter.convert import convert_code

# Load environment
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Load custom CSS
def load_css(file_path):
    try:
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ style.css not found!")

load_css("web_app/style.css")

# Streamlit UI
st.title("🔄 LangConvertor - AI Code Converter")
st.markdown("Easily convert code between programming languages using OpenRouter (Free API)")

code_input = st.text_area("✍️ Enter your code:", height=200)
source_lang = st.selectbox("🧩 Source Language", ["Python", "Java", "C++", "JavaScript"])
target_lang = st.selectbox("🎯 Target Language", ["Python", "Java", "C++", "JavaScript"])

if st.button("🚀 Convert"):
    if not code_input.strip():
        st.warning("Please enter some code.")
    elif source_lang == target_lang:
        st.warning("Source and target languages must be different.")
    else:
        with st.spinner("⏳ Converting..."):
            result = convert_code(code_input, source_lang, target_lang)
            st.markdown("### ✅ Converted Code:")
            st.code(result, language=target_lang.lower())
