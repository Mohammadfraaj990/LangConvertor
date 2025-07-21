import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from converter.convert import convert_code

# Load custom CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("web_app/style.css")

st.title("🔄 LangConvertor - AI Code Converter")
st.markdown("Easily convert code between languages using OpenRouter AI (Free API).")

code_input = st.text_area("✍️ Enter your code:", height=200)
source_lang = st.selectbox("🧩 Source Language", ["Python", "Java", "C++", "JavaScript"])
target_lang = st.selectbox("🎯 Target Language", ["Python", "Java", "C++", "JavaScript"])

if st.button("🚀 Convert"):
    if not code_input.strip():
        st.warning("Please enter your code.")
    elif source_lang == target_lang:
        st.warning("Source and target languages must be different.")
    else:
        with st.spinner("⏳ Converting..."):
            result = convert_code(code_input, source_lang, target_lang)
            st.markdown("### ✅ Converted Code:")
            st.code(result, language=target_lang.lower())
