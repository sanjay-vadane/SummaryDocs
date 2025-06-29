import streamlit as st
import openai
import os
from utils import load_document, save_summary
from summarizer import Summarizer

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.title("OpenAI Document Summarizer")
    
    uploaded_file = st.file_uploader("Choose a document", type=["txt", "pdf", "docx"])
    
    if uploaded_file is not None:
        text = load_document(uploaded_file)
        summarizer = Summarizer()
        summary = summarizer.summarize_text(text)
        
        st.subheader("Summary")
        st.write(summary)
        
        if st.button("Download Summary"):
            output_path = "summary.txt"
            save_summary(summary, output_path)
            with open(output_path, "rb") as file:
                st.download_button("Download", file, file_name="summary.txt")

if __name__ == "__main__":
    main()