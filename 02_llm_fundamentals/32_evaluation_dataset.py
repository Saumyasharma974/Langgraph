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

    # --------------------------------------
    # Clearly Positive
    # --------------------------------------

    {
        "input": "I love this product.",
        "expected": "Positive",
        "category": "Clear Positive"
    },

    {
        "input": "The service was excellent.",
        "expected": "Positive",
        "category": "Clear Positive"
    },

    {
        "input": "I am very happy with my purchase.",
        "expected": "Positive",
        "category": "Clear Positive"
    },

    {
        "input": "The experience was amazing.",
        "expected": "Positive",
        "category": "Clear Positive"
    },

    {
        "input": "I really enjoyed using this product.",
        "expected": "Positive",
        "category": "Clear Positive"
    },


    # --------------------------------------
    # Clearly Negative
    # --------------------------------------

    {
        "input": "This product is terrible.",
        "expected": "Negative",
        "category": "Clear Negative"
    },

    {
        "input": "I hate this service.",
        "expected": "Negative",
        "category": "Clear Negative"
    },

    {
        "input": "This was a disappointing experience.",
        "expected": "Negative",
        "category": "Clear Negative"
    },

    {
        "input": "I would never recommend this product.",
        "expected": "Negative",
        "category": "Clear Negative"
    },

    {
        "input": "The product completely failed to meet my expectations.",
        "expected": "Negative",
        "category": "Clear Negative"
    },


    # --------------------------------------
    # Edge / Ambiguous Cases
    # --------------------------------------

    {
        "input": "The product is okay.",
        "expected": "Positive",
        "category": "Edge Case"
    },

    {
        "input": "It's fine, I guess.",
        "expected": "Positive",
        "category": "Edge Case"
    },

    {
        "input": "Could be better.",
        "expected": "Negative",
        "category": "Edge Case"
    },

    {
        "input": "It works, but nothing special.",
        "expected": "Positive",
        "category": "Edge Case"
    },

    {
        "input": "Not bad, but I expected more.",
        "expected": "Negative",
        "category": "Edge Case"
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

Rules:

- Positive means the user expresses a positive
  or generally satisfactory experience.
- Negative means the user expresses dissatisfaction,
  disappointment, dislike, or a clearly negative experience.
- For ambiguous cases, follow the classification
  examples and rules above.
- Return ONLY one word:
  Positive
  or
  Negative

Text:
{text}
"""

    response = llm.invoke(prompt)

    return response.content.strip()


# ==========================================
# 5. Evaluation
# ==========================================

correct = 0
failures = []


print("=" * 60)
print("EVALUATION DATASET")
print("=" * 60)


for index, test_case in enumerate(test_cases, start=1):

    text = test_case["input"]
    expected = test_case["expected"]
    category = test_case["category"]

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
            "predicted": predicted,
            "category": category
        })

    print(f"\nTest {index}")
    print("Category:  ", category)
    print("Input:     ", text)
    print("Expected:  ", expected)
    print("Predicted: ", predicted)
    print("Result:    ", result)


# ==========================================
# 6. Overall Accuracy
# ==========================================

total = len(test_cases)

accuracy = (correct / total) * 100


print("\n" + "=" * 60)
print("OVERALL RESULT")
print("=" * 60)

print(f"Correct Predictions: {correct}/{total}")
print(f"Accuracy: {accuracy:.2f}%")


# ==========================================
# 7. Failure Analysis
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

        print("Category:")
        print(failure["category"])

        print("Expected:")
        print(failure["expected"])

        print("Predicted:")
        print(failure["predicted"])


# ==========================================
# 8. Category-wise Evaluation
# ==========================================

print("\n" + "=" * 60)
print("CATEGORY-WISE EVALUATION")
print("=" * 60)


categories = [
    "Clear Positive",
    "Clear Negative",
    "Edge Case"
]


for category in categories:

    category_cases = [
        case for case in test_cases
        if case["category"] == category
    ]

    category_correct = 0

    for case in category_cases:

        predicted = predict_sentiment(case["input"])

        if predicted.lower() == case["expected"].lower():
            category_correct += 1

    category_accuracy = (
        category_correct / len(category_cases)
    ) * 100

    print(
        f"{category}: "
        f"{category_correct}/{len(category_cases)} "
        f"({category_accuracy:.2f}%)"
    )