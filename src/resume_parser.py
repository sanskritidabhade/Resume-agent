from docx import Document
import os

def read_resume(file_path: str) -> str:
    # Reads a resume from .docx or .txt and returns plain text

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    
    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
        
    else:
        raise ValueError("❌ Unsupported file format. Use .docx or .txt")