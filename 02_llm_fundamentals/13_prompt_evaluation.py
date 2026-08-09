import os

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
# 2. Create LLM
# ==========================================

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    api_key=api_key,
    temperature=0
)


# ==========================================
# 3. Evaluation Dataset
# ==========================================

test_cases = [
    {
        "input": "I love this product.",
        "expected": "Positive"
    },
    {
        "input": "This product is terrible.",
        "expected": "Negative"
    },
    {
        "input": "The experience was amazing.",
        "expected": "Positive"
    },
    {
        "input": "I hate this service.",
        "expected": "Negative"
    },
    {
        "input": "The product is okay.",
        "expected": "Positive"
    },
    {
        "input": "I really enjoyed it.",
        "expected": "Positive"
    },
    {
        "input": "This was a disappointing experience.",
        "expected": "Negative"
    },
    {
        "input": "The service was excellent.",
        "expected": "Positive"
    },
    {
        "input": "I would never recommend this product.",
        "expected": "Negative"
    },
    {
        "input": "I am very happy with my purchase.",
        "expected": "Positive"
    }
]


# ==========================================
# 4. Prompt V1
# ==========================================

prompt_v1 = """
You are a sentiment classification assistant.

Task:
Classify the given sentence into one of two categories:

Positive
Negative

Constraints:
- Return only one category.
- Do not provide an explanation.
- Do not rewrite the sentence.
- Do not use any other category.

Output Format:
Positive
OR
Negative
"""


# ==========================================
# 5. Prompt V2
# ==========================================

prompt_v2 = """
You are an expert sentiment classification assistant.

Task:
Classify the given sentence as either Positive or Negative.

Definitions:

Positive:
The sentence expresses happiness, satisfaction,
enjoyment, approval, praise, or a favorable opinion.

Negative:
The sentence expresses dislike, dissatisfaction,
anger, disappointment, criticism, or an unfavorable opinion.

Examples:

Sentence: I love this product.
Category: Positive

Sentence: This product is terrible.
Category: Negative

Sentence: I really enjoyed the experience.
Category: Positive

Sentence: I hate this service.
Category: Negative

Sentence: I would never recommend this product.
Category: Negative

Rules:
- Carefully identify the overall sentiment.
- Consider the meaning of the complete sentence.
- Do not focus on a single word.
- Return only Positive or Negative.
- Do not provide an explanation.
- Do not rewrite the sentence.
- Never return any other category.

Output Format:
Positive
OR
Negative
"""


# ==========================================
# 6. Evaluation Function
# ==========================================

def evaluate_prompt(prompt, prompt_name):

    correct = 0
    total = len(test_cases)

    print("\n==========================================")
    print(prompt_name)
    print("==========================================\n")

    for index, test_case in enumerate(test_cases, start=1):

        final_prompt = f"""
{prompt}

Sentence:
{test_case["input"]}
"""

        response = llm.invoke(final_prompt)

        predicted = response.content.strip()
        expected = test_case["expected"]

        if predicted.lower() == expected.lower():
            result = "✅ Correct"
            correct += 1
        else:
            result = "❌ Incorrect"

        print(f"Test {index}")
        print(f"Input:      {test_case['input']}")
        print(f"Expected:   {expected}")
        print(f"Predicted:  {predicted}")
        print(f"Result:     {result}")
        print("-" * 50)

    accuracy = (correct / total) * 100

    print(f"\nCorrect Predictions: {correct}/{total}")
    print(f"Accuracy: {accuracy:.2f}%")

    return accuracy


# ==========================================
# 7. Evaluate Prompt V1
# ==========================================

accuracy_v1 = evaluate_prompt(
    prompt_v1,
    "PROMPT V1"
)


# ==========================================
# 8. Evaluate Prompt V2
# ==========================================

accuracy_v2 = evaluate_prompt(
    prompt_v2,
    "PROMPT V2"
)


# ==========================================
# 9. Compare Results
# ==========================================

print("\n==========================================")
print("          PROMPT COMPARISON")
print("==========================================")

print(f"Prompt V1 Accuracy: {accuracy_v1:.2f}%")
print(f"Prompt V2 Accuracy: {accuracy_v2:.2f}%")

difference = accuracy_v2 - accuracy_v1

print(f"Improvement: {difference:+.2f}%")