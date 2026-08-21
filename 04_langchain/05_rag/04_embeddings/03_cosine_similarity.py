from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# Create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Documents
documents = [
    "JWT is used for authentication and user verification.",
    "Python is a popular programming language.",
    "MongoDB is a NoSQL database used to store data."
]

# User query
query = "How does an application verify a user?"

# Convert documents into vectors
document_vectors = embeddings.embed_documents(documents)

# Convert query into vector
query_vector = embeddings.embed_query(query)

# Calculate cosine similarity
scores = cosine_similarity(
    [query_vector],
    document_vectors
)[0]

print("QUERY:")
print(query)

print("\nSIMILARITY SCORES:")

for i, score in enumerate(scores):
    print(f"\nDOCUMENT {i + 1}:")
    print(documents[i])
    print(f"Score: {score:.4f}")

# Find most similar document
best_index = scores.argmax()

print("\n" + "=" * 50)

print("MOST RELEVANT DOCUMENT:")
print(documents[best_index])

print(f"\nBEST SCORE: {scores[best_index]:.4f}")