import json
import os
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LocalVectorStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

class VectorStoreIndex:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    @classmethod
    def from_vector_store(cls, vector_store):
        vectors = vector_store.load()
        return cls(vectors)

    def as_chat_engine(self, service_context, chat_mode, system_prompt, verbose, llm, similarity_top_k):
        return ChatEngine(
            vectors=self.vector_store,
            service_context=service_context,
            chat_mode=chat_mode,
            system_prompt=system_prompt,
            verbose=verbose,
            llm=llm,
            similarity_top_k=similarity_top_k
        )

class ChatEngine:
    def __init__(self, vectors, service_context, chat_mode, system_prompt, verbose, llm, similarity_top_k):
        self.vectors = vectors
        self.service_context = service_context
        self.chat_mode = chat_mode
        self.system_prompt = system_prompt
        self.verbose = verbose
        self.llm = llm
        self.similarity_top_k = similarity_top_k

    async def astream_chat(self, query):
        # Implement the chat logic here
        response = f"Simulated response to query: {query}"
        return response

async def chat_with_chat_engine(self, query: str):
    logger.info("Chatting with chat engine")
    logger.info(query)

    # Load vector store from a local file
    local_vector_store = LocalVectorStore(file_path="local_vector_store.json")
    index = VectorStoreIndex.from_vector_store(local_vector_store)

    chat_engine = index.as_chat_engine(
        service_context=self.service_context,
        chat_mode="context",  # type: ignore
        system_prompt=(
            "You are a well informed private equity senior associate, whose job is review investment documents, market reports and then send well informed, succinct, data based answers."
            "You are professional. You do not say 'I do not know', you rather say 'I haven't found information related to this in the reports I read'. You never give information that wasn't provided to you in the context."
            "Give your answers in bullet point format. Be specific, do not make long sentences with verbose language."
            "\nInstructions: Use previous chat history to answer questions. If you are asked a question, you should answer it using the context information provided."
        ),
        verbose=True,
        llm=self.llm,
        similarity_top_k=5,
    )

    streaming_response = await chat_engine.astream_chat(query)

    return streaming_response