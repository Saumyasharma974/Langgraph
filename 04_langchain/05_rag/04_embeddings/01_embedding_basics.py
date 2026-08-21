from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Text we want to convert into an embedding
text = "JWT is used for authentication."

# Generate embedding
vector = embeddings.embed_query(text)

print("TEXT:")
print(text)

print("\nVECTOR:")
print(vector)

print("\nVECTOR TYPE:")
print(type(vector))

print("\nVECTOR LENGTH:")
print(len(vector))