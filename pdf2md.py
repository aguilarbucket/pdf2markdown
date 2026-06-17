import streamlit as st
from markitdown import MarkItDown
import tempfile

st.title("PDF → Markdown")

pdf = st.file_uploader("Sube un PDF", type=["pdf"])

if pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(pdf.read())
        pdf_path = f.name

    md = MarkItDown()
    result = md.convert(pdf_path)

    markdown = result.text_content

    st.text_area("Preview", markdown[:5000], height=300)

    st.download_button(
        "Descargar Markdown",
        markdown,
        file_name=pdf.name.replace(".pdf", ".md"),
        mime="text/markdown"
    )