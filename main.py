import os
import PyPDF2
from transformers import pipeline

# ✅ Set Hugging Face API Key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your-huggingface-api-key"

def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = [page.extract_text() for page in pdf_reader.pages if page.extract_text()]

        if not extracted_text:  # ✅ Check if the extracted text is empty
            raise ValueError("⚠️ No extractable text found in the PDF.")

        return "\n".join(extracted_text)
    
    except Exception as e:
        raise ValueError(f"❌ Error reading PDF: {str(e)}")

def hf_summarize(text):
    """Summarize text using Hugging Face's Transformers."""
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
        # ✅ Ensure text isn't too long for the model
        if len(text.split()) > 1024:
            text = " ".join(text.split()[:1024])  # Trim text to 1024 words

        summary = summarizer(text, max_length=500, min_length=300, do_sample=False)
        return summary[0]['summary_text']
    
    except Exception as e:
        raise RuntimeError(f"❌ Error in summarization: {str(e)}")

def summarizer(pdf_file):
    """Summarizer function using Hugging Face."""
    text = extract_text_from_pdf(pdf_file)

    if not text.strip():  # ✅ Ensure extracted text isn't empty
        return "⚠️ No text found in the PDF for summarization."

    return hf_summarize(text)
