from langchain_openai import ChatOpenAI
import os


from ragas.testset.prompts import (
    context_scoring_prompt,
    evolution_elimination_prompt,
    filter_question_prompt,
)
from langchain_community.document_loaders import DirectoryLoader
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from ragas.testset.filters import QuestionFilter, EvolutionFilter, NodeFilter
from ragas.llms import LangchainLLMWrapper


inference_server_url = "http://localhost:8000/v1"
MODEL = "explodinggradients/Ragas-critic-llm-Qwen1.5-GPTQ"
chat = ChatOpenAI(
    model=MODEL,
    openai_api_key="token-abc123",
    openai_api_base=inference_server_url,
    max_tokens=2048,
    temperature=0,
)

# remove demonstrations from examples
for prompt in [
    context_scoring_prompt,
    evolution_elimination_prompt,
    filter_question_prompt,
]:
    prompt.examples = []
    


langchain_llm = LangchainLLMWrapper(chat)

qa_filter = QuestionFilter(langchain_llm, filter_question_prompt)
node_filter = NodeFilter(langchain_llm, context_scoring_prompt=context_scoring_prompt)
evolution_filter = EvolutionFilter(langchain_llm, evolution_elimination_prompt)



distributions = {simple: 0.5, reasoning: 0.25, multi_context: 0.25}


# customise the filters
from ragas.testset.evolutions import ComplexEvolution

for evolution in distributions:
    if evolution.question_filter is None:
        evolution.question_filter = qa_filter
    if evolution.node_filter is None:
        evolution.node_filter = node_filter

    if isinstance(evolution, ComplexEvolution):
        if evolution.evolution_filter is None:
            evolution.evolution_filter = evolution_filter