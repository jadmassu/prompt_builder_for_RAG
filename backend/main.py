from flask import Flask
import os, sys
from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from data_loader import load_pdf, split_pdf,extract_text_from_pages
load_dotenv()
# llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
filePath = os.getenv("PATH_TO_PDF")

app = Flask(__name__)

@app.route("/generatePrompt")
def generate_prompt():
    loaded_data = load_pdf(filePath)
    sp =split_pdf(loaded_data)
   
    return  {"gen" : "hi"}