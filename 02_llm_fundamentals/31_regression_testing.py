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

PROMPT_V1 = """
Classify the following text as Positive or Negative.

Return only:
Positive
or
Negative

Text:
{text}
"""


# ==========================================
# 5. Prompt V2
# ==========================================

PROMPT_V2 = """
Classify the following text as Positive or Negative.

Rules:
- Positive includes positive, happy, enjoyable,
  satisfactory, or neutral/okay experiences.
- Negative includes unhappy, terrible, hateful,
  disappointing, or strongly dissatisfied experiences.
- Return exactly one word:
  Positive
  or
  Negative

Text:
{text}
"""


# ==========================================
# 6. Prediction Function
# ==========================================

def predict(prompt_template, text):

    prompt = prompt_template.format(text=text)

    response = llm.invoke(prompt)

    return response.content.strip()


# ==========================================
# 7. Evaluation Function
# ==========================================

def evaluate(prompt_template):

    correct = 0
    failures = []

    for test_case in test_cases:

        predicted = predict(
            prompt_template,
            test_case["input"]
        )

        expected = test_case["expected"]

        if predicted.lower() == expected.lower():

            correct += 1

        else:

            failures.append({
                "input": test_case["input"],
                "expected": expected,
                "predicted": predicted
            })

    accuracy = (correct / len(test_cases)) * 100

    return correct, accuracy, failures


# ==========================================
# 8. Evaluate Prompt V1
# ==========================================

print("=" * 60)
print("PROMPT V1")
print("=" * 60)

correct_v1, accuracy_v1, failures_v1 = evaluate(PROMPT_V1)

print(f"Correct: {correct_v1}/{len(test_cases)}")
print(f"Accuracy: {accuracy_v1:.2f}%")


# ==========================================
# 9. Evaluate Prompt V2
# ==========================================

print("\n" + "=" * 60)
print("PROMPT V2")
print("=" * 60)

correct_v2, accuracy_v2, failures_v2 = evaluate(PROMPT_V2)

print(f"Correct: {correct_v2}/{len(test_cases)}")
print(f"Accuracy: {accuracy_v2:.2f}%")


# ==========================================
# 10. Compare
# ==========================================

print("\n" + "=" * 60)
print("REGRESSION TEST RESULT")
print("=" * 60)

improvement = accuracy_v2 - accuracy_v1

print(f"Prompt V1 Accuracy: {accuracy_v1:.2f}%")
print(f"Prompt V2 Accuracy: {accuracy_v2:.2f}%")
print(f"Improvement: {improvement:+.2f}%")


# ==========================================
# 11. Failure Analysis
# ==========================================

print("\n" + "=" * 60)
print("V1 FAILURES")
print("=" * 60)

if not failures_v1:

    print("No failures.")

else:

    for failure in failures_v1:

        print(f"\nInput: {failure['input']}")
        print(f"Expected: {failure['expected']}")
        print(f"Predicted: {failure['predicted']}")


print("\n" + "=" * 60)
print("V2 FAILURES")
print("=" * 60)

if not failures_v2:

    print("No failures.")

else:

    for failure in failures_v2:

        print(f"\nInput: {failure['input']}")
        print(f"Expected: {failure['expected']}")
        print(f"Predicted: {failure['predicted']}")


# ==========================================
# 12. Regression Detection
# ==========================================

print("\n" + "=" * 60)
print("REGRESSION CHECK")
print("=" * 60)

if accuracy_v2 < accuracy_v1:

    print("❌ Regression detected.")
    print("Prompt V2 performed worse than Prompt V1.")

elif accuracy_v2 > accuracy_v1:

    print("✅ Improvement detected.")
    print("Prompt V2 performed better than Prompt V1.")

else:

    print("➡️ No accuracy change.")