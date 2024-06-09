from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter

class RAGProcessor:
    def __init__(self,  llm):
   
        self.llm = llm
        self.rag = None
        self.rag_chain = None

    def create_rag(self,vector_db):
        try:
            self.rag = vector_db.as_retriever(
                search_type="similarity_score_threshold", 
                search_kwargs={"score_threshold": 0.5}
            )
            return self.rag
        except Exception as e:
            raise RuntimeError(f"An error occurred while creating RAG: {e}")

    def generate_prompt_template(self):
        try:
            template = """Create a question based only on the following context, please respond with 'I don't know':
            {question}
            Context:
            {context}
            """

            prompt = ChatPromptTemplate.from_messages([("human", template)])
            return prompt
        except Exception as e:
            raise RuntimeError(f"An error occurred while generating response: {e}")

    def process_rag_chain(self):
        try:
            if self.rag is None:
                raise RuntimeError("RAG retriever is not initialized. Please create RAG first.")

            self.rag_chain = (
                {"context": itemgetter("question") | self.rag, "question": itemgetter("question")}
                | RunnablePassthrough.assign(context=itemgetter("context"))
                | {"response": self.generate_prompt_template() | self.llm, "context": itemgetter("context")}
            )
            return  self.rag_chain
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing RAG chain: {e}")

    def invoker(self, question):
        try:
            if self.rag_chain is None:
                raise RuntimeError("RAG chain is not initialized. Please process RAG chain first.")
            
            return self.rag_chain.invoke({"question": question})
        except Exception as e:
            raise RuntimeError(f"An error occurred while invoking the chain: {e}")
