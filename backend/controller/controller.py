import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from service.data_loader import load_pdf, split_pdf
from service.chroma_db_manager import ChromaDBManager
from langchain.text_splitter import RecursiveCharacterTextSplitter
from service.prompt_generetor import generate_prompt_template,process_rag_chain,invoker
load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("LLM",llm)
filePath = os.getenv("PATH_TO_PDF")

def controller(prompt):
    try:
        
        loaded_data = load_pdf(filePath)
        sp =split_pdf(loaded_data)
        # text_splitter2 = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)
        # documents = text_splitter2.split_documents(sp)    
        # print(len(documents))
        # print(documents[2])
        # print("-------------")
        # print(sp[2])
        croma = ChromaDBManager()
        croma.store_and_load_chroma_db(sp)
        # res = croma.search_chroma_db_with_score("what is the name of the grandmother")
        rag = croma.createRag()
        # template = generate_prompt_template()
        chain = process_rag_chain(llm)
        res = invoker(chain,rag,prompt)
        print("---------",res)
        return res
    except Exception as e:
        raise RuntimeError(f"error: {e}")