TOKEN_LIMIT = 10000
requests = [2000, 3000, 4000, 2500]

total_tokens = 0

for tokens in requests:

    if total_tokens + tokens <= TOKEN_LIMIT:
        total_tokens += tokens
        print("token limit appro")
    else:
        print("token limit exceeded")