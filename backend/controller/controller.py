import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from service.data_loader import load_pdf, split_pdf
from service.chroma_db_manager import ChromaDBManager
load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("LLM",llm)
filePath = os.getenv("PATH_TO_PDF")

def controller(prompt):
    try:
        
        loaded_data = load_pdf(filePath)
        sp =split_pdf(loaded_data)
        croma = ChromaDBManager()
        croma.store_and_load_chroma_db(sp)
        # res = croma.search_chroma_db_with_score("what is the name of the grandmother")
        croma.createRag()
        res = croma.invokeRag("what is the name of the grandmother")
        print("---------",res)
        return res
    except Exception as e:
        raise RuntimeError(f"error: {e}")