from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

class Chain:
    @staticmethod
    def create_chain(user_api_key, docs, QA_PROMPT):
        embeddings = OpenAIEmbeddings(openai_api_key=user_api_key)
        vectors = FAISS.from_documents(docs, embeddings)
        llm = ChatOpenAI()

        # Create the conversational retrieval chain
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectors.as_retriever(search_type="similarity", search_kwargs={"k":4}),
            verbose=True,
            return_source_documents=True,
            max_tokens_limit=4097,
            combine_docs_chain_kwargs={'prompt': QA_PROMPT}
        )

        return chain
