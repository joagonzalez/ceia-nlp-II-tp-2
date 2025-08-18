import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

DATASET = ["cv1.txt"]

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = "developer-quickstart-py"
PINECONE_LOAD_DATA = False
PINECONE_EMBEDDING_MODEL = "llama-text-embed-v2"
PINECONE_NAMESPACE = "example-namespace"
PINECONE_TOPK_SEARCH = 10

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_LLM_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
GROQ_MAX_COMPLETION_TOKENS = 1024
GROQ_TEMPERATURE = 1.0
GROQ_STREAM = True