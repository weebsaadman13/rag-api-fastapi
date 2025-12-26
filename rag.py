from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(temperature=0)

def generate_answer(question: str, docs):
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know."

Context:
{context}

Question:
{question}
"""

    response = llm([HumanMessage(content=prompt)])
    return response.content

