import streamlit as st
import os
import asyncio
from main import summarizer

# ✅ Ensure asyncio loop is set correctly
def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

# Call this before running Streamlit
ensure_event_loop()

def main():
    st.set_page_config(page_title="PDF Summarizer")
    st.title("📄 PDF Summarizer App")

    st.write("Summarize your PDF files in just a few seconds! ")
    st.divider()

    pdf_file = st.file_uploader("📂 Upload your PDF document", type="pdf")

    # ✅ Set Hugging Face API Key
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if st.button("📝 Generate Summary"):
        if pdf_file is not None:
            try:
                response = summarizer(pdf_file)
                st.subheader("📃 Summary of File:")
                st.write(response)
            except Exception as e:
                st.error(f"❌ Error processing the PDF: {str(e)}")
        else:
            st.warning("⚠️ Please upload a PDF file first.")

if __name__ == "__main__":
    main()
