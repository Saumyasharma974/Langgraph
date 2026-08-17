from langchain_community.document_loaders import TextLoader


# -----------------------------------
# CREATE LOADER
# -----------------------------------

loader = TextLoader("auth_notes.txt")


# -----------------------------------
# LOAD DOCUMENT
# -----------------------------------

documents = loader.load()


# -----------------------------------
# PRINT DOCUMENTS
# -----------------------------------

print("DOCUMENTS:")
print(documents)


# -----------------------------------
# NUMBER OF DOCUMENTS
# -----------------------------------

print("\nNUMBER OF DOCUMENTS:")
print(len(documents))


# -----------------------------------
# FIRST DOCUMENT
# -----------------------------------

doc = documents[0]

print("\nPAGE CONTENT:")
print(doc.page_content)

print("\nMETADATA:")
print(doc.metadata)


# -----------------------------------
# TYPE
# -----------------------------------

print("\nDOCUMENT TYPE:")
print(type(doc))