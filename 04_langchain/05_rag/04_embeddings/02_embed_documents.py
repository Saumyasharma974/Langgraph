from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "JWT is used for authentication.",
    "Python is a programming language.",
    "MongoDB is a NoSQL database."
]

vectors = embeddings.embed_documents(documents)

print("NUMBER OF DOCUMENTS:")
print(len(documents))

print("\nNUMBER OF VECTORS:")
print(len(vectors))

print("\nVECTOR TYPE:")
print(type(vectors))

print("\nFIRST VECTOR TYPE:")
print(type(vectors[0]))

print("\nVECTOR DIMENSION:")
print(len(vectors[0]))

print("\nFIRST 10 VALUES OF EACH VECTOR:")

for i, vector in enumerate(vectors):
    print(f"\nDOCUMENT {i + 1}:")
    print(documents[i])
    print(vector[:10])