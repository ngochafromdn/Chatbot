from langchain.prompts.prompt import PromptTemplate
class prompt():
    @staticmethod
    def generate_qa_prompt():
        qa_template = """
            You are a helpful AI assistant of Smartjen. The user gives you a link which includes the content, use them to answer the question at the end.
            If you don't know the answer, just say you don't know. Do NOT try to make up an answer.
            If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to the context.
            Use as much detail as possible when responding.

            context: {context}
            =========
            question: {question}
            ======
            """

        qa_prompt = PromptTemplate(template=qa_template, input_variables=["context", "question"])
        return qa_prompt
