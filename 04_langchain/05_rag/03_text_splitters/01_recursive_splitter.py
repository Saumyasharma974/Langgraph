from langchain_text_splitters import RecursiveCharacterTextSplitter
text = (
    "JWT authentication is used to verify users. "
    "The user logs into the application with credentials. "
    "The server validates those credentials. "
    "The server generates a JSON Web Token. "
    "The token contains a header, payload, and signature. "
    "The server signs the token using a secret key. "
    "The client sends the token with future requests. "
    "The server verifies the token before allowing access. "
    "JWT is commonly used in APIs and web applications."
)

# -----------------------------------
# CREATE TEXT SPLITTER
# -----------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)


# -----------------------------------
# SPLIT TEXT
# -----------------------------------

chunks = splitter.split_text(text)


# -----------------------------------
# PRINT RESULT
# -----------------------------------

print("NUMBER OF CHUNKS:")
print(len(chunks))


for i, chunk in enumerate(chunks):

    print(f"\n========== CHUNK {i + 1} ==========")

    print(chunk)

    print("\nCHUNK LENGTH:")
    print(len(chunk))