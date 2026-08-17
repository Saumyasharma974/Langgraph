from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# -----------------------------------
# TEXT
# -----------------------------------

text = (
    "JWT authentication is used to verify users. "
    "The user logs into the application with credentials. "
    "The server validates those credentials. "
    "The server generates a JSON Web Token. "
    "The token contains a header, payload, and signature."
)


# -----------------------------------
# SPLITTER
# -----------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)


# ===================================
# 1. split_text()
# ===================================

text_chunks = splitter.split_text(text)

print("========== split_text() ==========")

print("TYPE:")
print(type(text_chunks))

print("NUMBER OF CHUNKS:")
print(len(text_chunks))

for i, chunk in enumerate(text_chunks):
    print(f"\nCHUNK {i + 1}:")
    print(chunk)


# ===================================
# 2. create_documents()
# ===================================

created_documents = splitter.create_documents(
    [text]
)

print("\n\n========== create_documents() ==========")

print("TYPE:")
print(type(created_documents))

print("NUMBER OF DOCUMENTS:")
print(len(created_documents))

for i, doc in enumerate(created_documents):

    print(f"\nDOCUMENT {i + 1}:")

    print("CONTENT:")
    print(doc.page_content)

    print("METADATA:")
    print(doc.metadata)


# ===================================
# 3. split_documents()
# ===================================

documents = [
    Document(
        page_content=text,
        metadata={
            "source": "auth_notes.txt",
            "topic": "JWT"
        }
    )
]

split_documents = splitter.split_documents(documents)

print("\n\n========== split_documents() ==========")

print("TYPE:")
print(type(split_documents))

print("NUMBER OF DOCUMENTS:")
print(len(split_documents))

for i, doc in enumerate(split_documents):

    print(f"\nDOCUMENT {i + 1}:")

    print("CONTENT:")
    print(doc.page_content)

    print("METADATA:")
    print(doc.metadata)