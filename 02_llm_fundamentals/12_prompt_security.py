import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


# ==========================================
# 2. Create Groq LLM
# ==========================================

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)


# ==========================================
# 3. Define Structured Output
# ==========================================

class RefundRequest(BaseModel):
    amount: float = Field(
        description="Refund amount requested by the customer"
    )

    reason: str = Field(
        description="Reason for requesting the refund"
    )


# ==========================================
# 4. Configure Structured Output
# ==========================================

structured_llm = llm.with_structured_output(
    RefundRequest
)


# ==========================================
# 5. Get User Request
# ==========================================

user_request = input(
    "Enter your refund request: "
)


# ==========================================
# 6. Create Prompt
# ==========================================

prompt = f"""
Extract the refund information from the
customer request.

Return:
- refund amount
- refund reason

Do not invent information.

Customer request:
{user_request}
"""


# ==========================================
# 7. Get Structured Response
# ==========================================

result = structured_llm.invoke(prompt)


# ==========================================
# 8. Display Extracted Information
# ==========================================

print("\n========================================")
print("        REFUND INFORMATION")
print("========================================")

print(f"Amount: ₹{result.amount}")
print(f"Reason: {result.reason}")


# ==========================================
# 9. Security Rule
# ==========================================

print("\n========================================")
print("          SECURITY CHECK")
print("========================================")

if result.amount <= 10000:
    print("✅ Refund Allowed")

else:
    print("⚠️ Human Approval Required")