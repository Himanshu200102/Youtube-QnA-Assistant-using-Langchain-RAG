from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Use sentence-transformers for semantic embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load and vectorize transcript
def vector_db_video_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db

# Run query against vector DB
def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page = " ".join([d.page_content for d in docs])

    # Load LLM
    llm = Ollama(model="llama2", temperature=0.0)  # Lower temp = less hallucination

    # Grounded prompt
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
You are a helpful assistant for summarizing and answering questions based on YouTube video transcripts.

Use ONLY the information from the transcript context below to answer the question.

Transcript context:
{docs}

Question:
{question}

Rules:
- If the answer is not in the transcript, say: "I couldn't find that in the video."
- Do NOT make up any facts or provide personal opinions.
- Keep the answer concise and factual.
- Instead of sayin transcript say video.
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(question=query, docs=docs_page)
    return response.strip(), docs
