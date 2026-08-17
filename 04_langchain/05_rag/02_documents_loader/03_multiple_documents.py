from langchain_core.documents import Document


# -----------------------------------
# CREATE MULTIPLE DOCUMENTS
# -----------------------------------

documents = [

    Document(
        page_content="JWT is used for authentication.",
        metadata={
            "source": "auth_notes.txt",
            "topic": "JWT"
        }
    ),

    Document(
        page_content="Docker packages applications into containers.",
        metadata={
            "source": "docker_notes.txt",
            "topic": "Docker"
        }
    ),

    Document(
        page_content="RAG retrieves relevant information before generating an answer.",
        metadata={
            "source": "rag_notes.txt",
            "topic": "RAG"
        }
    )
]


# -----------------------------------
# NUMBER OF DOCUMENTS
# -----------------------------------

print("NUMBER OF DOCUMENTS:")
print(len(documents))


# -----------------------------------
# PRINT EACH DOCUMENT
# -----------------------------------

for index, doc in enumerate(documents):

    print(f"\n========== DOCUMENT {index + 1} ==========")

    print("\nCONTENT:")
    print(doc.page_content)

    print("\nMETADATA:")
    print(doc.metadata)