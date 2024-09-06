import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from service.file_processor import FileProcessor
from service.chroma_db_manager import ChromaDBManager
from service.rag_processor import RAGProcessor
load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
filePath = os.getenv("PATH_TO_TXT")

def controller(prompt):
    try:
        file = FileProcessor(filePath)
        file.load_file()
        sp = file.split_file()
       
        chroma = ChromaDBManager()
        chromadb = chroma.store_and_load_chroma_db(sp)
       
        rag_processor = RAGProcessor(llm)
        rag =rag_processor.create_rag(chromadb)
      
        rag_processor.process_rag_chain()
        res = rag_processor.invoker(prompt)
        print(res)
        return res["response"].content
    except Exception as e:
        raise RuntimeError(f"error: {e}")