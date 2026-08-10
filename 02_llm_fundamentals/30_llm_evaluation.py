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
# 4. Prediction Function
# ==========================================

def predict_sentiment(text):

    prompt = f"""
Classify the following text as exactly one of:

Positive
Negative

Text:
{text}

Return only:
Positive
or
Negative
"""

    response = llm.invoke(prompt)

    return response.content.strip()


# ==========================================
# 5. Run Evaluation
# ==========================================

correct = 0
failures = []


print("=" * 60)
print("LLM EVALUATION")
print("=" * 60)


for index, test_case in enumerate(test_cases, start=1):

    text = test_case["input"]
    expected = test_case["expected"]

    predicted = predict_sentiment(text)

    is_correct = predicted.lower() == expected.lower()

    if is_correct:
        correct += 1
        result = "✅ Correct"

    else:
        result = "❌ Incorrect"

        failures.append({
            "input": text,
            "expected": expected,
            "predicted": predicted
        })

    print(f"\nTest {index}")
    print("Input:     ", text)
    print("Expected:  ", expected)
    print("Predicted: ", predicted)
    print("Result:    ", result)


# ==========================================
# 6. Calculate Accuracy
# ==========================================

total = len(test_cases)

accuracy = (correct / total) * 100


# ==========================================
# 7. Final Evaluation
# ==========================================

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print(f"Correct Predictions: {correct}/{total}")
print(f"Accuracy: {accuracy:.2f}%")


# ==========================================
# 8. Failure Analysis
# ==========================================

print("\n" + "=" * 60)
print("FAILURE ANALYSIS")
print("=" * 60)


if not failures:

    print("No failures found. 🎉")

else:

    for failure in failures:

        print("\nInput:")
        print(failure["input"])

        print("Expected:")
        print(failure["expected"])

        print("Predicted:")
        print(failure["predicted"])