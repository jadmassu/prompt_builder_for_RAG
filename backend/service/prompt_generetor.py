
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
def generate_prompt_template():
    try:
        template = """
        Create a question based only on the following context, please respond with 'I don't know':
        Context: {context}
        Question: {question}
        
        """

        prompt = ChatPromptTemplate.from_template(template)
        return prompt
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating response: {e}")
def process_rag_chain(llm):
    try:
        rag_chain = (
             generate_prompt_template()
            | llm
            | StrOutputParser()
        )
        return rag_chain
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing rag chain: {e}")

def invoker(chain, context , question):
    
    response = chain.invoke({
        "context": context,
        "question": question
        })
    
    return response