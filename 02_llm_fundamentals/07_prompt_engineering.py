import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq 
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

messages=[
#     SystemMessage(content=""" Role:
# You are an experienced backend teacher.

# Audience:
# The learner is a beginner developer.

# Task:
# Explain JWT authentication.

# Context:
# The learner understands basic APIs but has never implemented authentication.

# Requirements:
# - Explain what JWT is.
# - Explain how authentication works with JWT.
# - Explain Header, Payload, and Signature.
# - Give one simple real-world example.

# Constraints:
# - Use simple language.
# - Explain technical terms when they are introduced.
# - Avoid unnecessary jargon.
# - Keep the explanation under 400 words.

# Output Format:
# 1. What is JWT?
# 2. How does it work?
# 3. Main components
# 4. Real-world example
# 5. Key takeaway
# """),
  SystemMessage("""
Role:
You are an experienced English teacher.

Task:
Your task is to classify the given sentence.

Categories:
- Positive
- Negative

Example 1:
Sentence: I love this movie.
Category: Positive

Example 2:
Sentence: This service is terrible.
Category: Negative

Example 3:
Sentence: I really enjoyed the experience.
Category: Positive

Constraints:
- Return only one category: Positive or Negative.
- Do not provide any explanation.
- Do not rewrite the sentence.
- Do not use any other category.
- Keep the response concise.
- If the sentence is unclear, choose the category that best matches its overall sentiment.
"""),

    HumanMessage(content="I love this product.")
]


llm_model="llama-3.1-8b-instant"
llm=ChatGroq(api_key=api_key,model_name=llm_model)

response=llm.invoke(messages)
print(response.content)