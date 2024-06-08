import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from service.file_processor import FileProcessor
from service.chroma_db_manager import ChromaDBManager
from service.rag_processor import RAGProcessor
load_dotenv()

class Controller:
    def __init__(self):
        self.llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.file_path = os.getenv("PATH_TO_TXT")
        self.rag_processor = None

    def generate_prompt(self, prompt):
        try:
            res = self.rag_processor.invoker(prompt)
            print(res)
            return res["response"].content
        except Exception as e:
            raise RuntimeError(f"error: {e}")

    def init_process(self):
        try:
            file = FileProcessor(self.file_path)
            file.load_file()
            sp = file.split_file()
       
            chroma = ChromaDBManager()
            chromadb = chroma.store_and_load_chroma_db(sp)
            self.rag_processor = RAGProcessor(self.llm)
            rag = self.rag_processor.create_rag(chromadb)
      
            self.rag_processor.process_rag_chain()
        except Exception as e:
            raise RuntimeError(f"error: {e}")

    def evaluate(self):
        try:
            print(self.evaluate)
        except Exception as e:
            raise RuntimeError(f"error: {e}")


