from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

def create_vector_store(chunks, metadata):
    return FAISS.from_texts(
        texts = chunks,
        embedding = embeddings,
        metadatas = metadata 
    )

