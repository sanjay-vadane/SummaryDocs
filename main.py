# filepath: [main.py](http://_vscodecontentref_/0)
import io
from PyPDF2 import PdfReader
import docx
import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("OpenAI Document Summarizer")

def load_document(file_bytes, file_type=None):
    if file_type == "pdf":
        reader = PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif file_type == "docx":
        doc = docx.Document(io.BytesIO(file_bytes))
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    else:
        # Assume plain text
        return file_bytes.decode("utf-8")
def summarize_text(text):
    client = openai.OpenAI()
    prompt = (
        "Summarize the following document in 3 lines, covering the main points:\n\n"
        + text
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.5,
    )
    summary = response.choices[0].message.content.strip()
    return summary

uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    file_name = uploaded_file.name

    if file_name.endswith(".pdf"):
        text = load_document(file_bytes, file_type="pdf")
    elif file_name.endswith(".docx"):
        text = load_document(file_bytes, file_type="docx")
    else:
        text = load_document(file_bytes, file_type="txt")

    st.subheader("Document Content")
    st.write(text[:1000])  # Show only the first 1000 characters for preview

    if st.button("Summarize Document"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
        st.subheader("3-Line Summary")
        st.write(summary)