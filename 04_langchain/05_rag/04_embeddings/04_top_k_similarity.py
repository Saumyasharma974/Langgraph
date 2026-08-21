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
    "JWT contains a header, payload, and signature.",
    "Python is a popular programming language.",
    "MongoDB is a NoSQL database used to store data.",
    "JWT tokens are commonly used to secure APIs."
]

# User query
query = "How does JWT help with authentication?"

# Convert documents into vectors
document_vectors = embeddings.embed_documents(documents)

# Convert query into a vector
query_vector = embeddings.embed_query(query)

# Calculate similarity scores
scores = cosine_similarity(
    [query_vector],
    document_vectors
)[0]

# Number of top results we want
k = 3

# Get indices sorted from highest score to lowest
top_indices = scores.argsort()[::-1][:k]

print("QUERY:")
print(query)

print("\n" + "=" * 50)
print(f"TOP {k} MOST RELEVANT DOCUMENTS")
print("=" * 50)

for rank, index in enumerate(top_indices, start=1):
    print(f"\nRANK {rank}")
    print("DOCUMENT:")
    print(documents[index])
    print(f"SIMILARITY SCORE: {scores[index]:.4f}")