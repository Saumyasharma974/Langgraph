from langchain_core.documents import Document
from pypdf import PdfReader


# -----------------------------------
# LOAD PDF
# -----------------------------------

reader = PdfReader("Dsanotes.pdf")


# -----------------------------------
# CREATE DOCUMENTS
# -----------------------------------

documents = []

for page_number, page in enumerate(reader.pages):

    text = page.extract_text()

    if text:
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": "Dsanotes.pdf",
                    "page": page_number
                }
            )
        )


# -----------------------------------
# INFORMATION
# -----------------------------------

print("NUMBER OF DOCUMENTS:")
print(len(documents))


# -----------------------------------
# PRINT EACH DOCUMENT
# -----------------------------------

for i, doc in enumerate(documents):

    print(f"\n========== DOCUMENT {i + 1} ==========")

    print("\nPAGE CONTENT:")
    print(doc.page_content)

    print("\nMETADATA:")
    print(doc.metadata)