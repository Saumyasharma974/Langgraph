from langchain_core.documents import Document


doc = Document(
    page_content="JWT is used for authentication.",
    metadata={
        "source": "auth_notes.txt",
        "topic": "JWT"
    }
)


print("DOCUMENT:")
print(doc)

print("\nPAGE CONTENT:")
print(doc.page_content)

print("\nMETADATA:")
print(doc.metadata)

print("\nDOCUMENT TYPE:")
print(type(doc))

print("\nPAGE CONTENT TYPE:")
print(type(doc.page_content))

print("\nMETADATA TYPE:")
print(type(doc.metadata))