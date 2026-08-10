# import os

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq


# # ==========================================
# # 1. Load Environment Variables
# # ==========================================

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# if not api_key:
#     raise ValueError("GROQ_API_KEY is missing")


# # ==========================================
# # 2. Create Models
# # ==========================================

# # Model A - Fast / Simple Tasks
# model_a = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     api_key=api_key,
#     temperature=0
# )

# # Model B - More Capable Task
# model_b = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     api_key=api_key,
#     temperature=0
# )


# # ==========================================
# # 3. Simple Task
# # ==========================================

# print("=" * 50)
# print("MODEL A - SIMPLE TASK")
# print("=" * 50)

# response_a = model_a.invoke(
#     "Classify this message as Positive or Negative: "
#     "I really enjoyed this product."
# )

# print(response_a.content)

# print("\nToken Usage:")
# print(response_a.response_metadata.get("token_usage"))


# # ==========================================
# # 4. Complex Task
# # ==========================================

# print("\n" + "=" * 50)
# print("MODEL B - COMPLEX TASK")
# print("=" * 50)

# response_b = model_b.invoke(
#     """
#     Analyze this customer complaint:

#     "I purchased a laptop last week. The laptop becomes
#     extremely slow after 30 minutes, the battery drains quickly,
#     and customer support has not responded to my emails."

#     Identify:
#     1. Main problem
#     2. Possible root causes
#     3. Customer impact
#     4. Recommended solution
#     """
# )

# print(response_b.content)

# print("\nToken Usage:")
# print(response_b.response_metadata.get("token_usage"))


import os
import time

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# ==========================================
# 2. Create Two Different Groq Models
# ==========================================

# Model A - Smaller / Faster / Lower Cost
model_a = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)


# Model B - Larger / More Capable / Higher Cost
model_b = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0
)


# ==========================================
# 3. Same Simple Task
# ==========================================

prompt = """
Classify this message as Positive or Negative.

Message:
I really enjoyed this product.
"""


# ==========================================
# 4. Model A
# ==========================================

print("=" * 60)
print("MODEL A - LLAMA 3.1 8B INSTANT")
print("=" * 60)

start = time.perf_counter()

response_a = model_a.invoke(prompt)

end = time.perf_counter()

usage_a = response_a.response_metadata["token_usage"]

print("\nResponse:")
print(response_a.content)

print("\nToken Usage:")
print(usage_a)

print("\nLatency:")
print(f"{end - start:.4f} seconds")


# ==========================================
# 5. Model B
# ==========================================

print("\n" + "=" * 60)
print("MODEL B - LLAMA 3.3 70B VERSATILE")
print("=" * 60)

start = time.perf_counter()

response_b = model_b.invoke(prompt)

end = time.perf_counter()

usage_b = response_b.response_metadata["token_usage"]

print("\nResponse:")
print(response_b.content)

print("\nToken Usage:")
print(usage_b)

print("\nLatency:")
print(f"{end - start:.4f} seconds")


# ==========================================
# 6. Comparison
# ==========================================

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print("\nModel A:")
print("llama-3.1-8b-instant")
print("Total Tokens:", usage_a["total_tokens"])

print("\nModel B:")
print("llama-3.3-70b-versatile")
print("Total Tokens:", usage_b["total_tokens"])