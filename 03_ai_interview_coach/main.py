from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from config import MAX_QUESTIONS
from models.feedback import InterviewFeedback
from services.question_generator import generate_first_question, generate_next_question
from services.evaluator import evaluate_answer

# ============================================================
# 1. DISPLAY FEEDBACK
# ============================================================

def display_feedback(feedback: InterviewFeedback):
    print("\n========================================")
    print("             FEEDBACK")
    print("========================================")
    print(f"\nScore: {feedback.score}/10")
    print(f"Correct: {feedback.correct}")
    
    print("\nStrengths:")
    for strength in feedback.strengths:
        print(f"  ✓ {strength}")
        
    print("\nWeaknesses:")
    for weakness in feedback.weaknesses:
        print(f"  ✗ {weakness}")
        
    print("\nImprovement:")
    print(f"  {feedback.improvement}")
    
    print("\nNext Action:")
    print(f"  {feedback.next_action}")


# ============================================================
# 2. MAIN
# ============================================================

def main():
    print("\n========================================")
    print("          AI INTERVIEW COACH")
    print("========================================")

    print("\nChoose Interview Type:\n")
    print("1. DSA")
    print("2. Backend")
    print("3. Python")
    print("4. AI/ML")
    print("5. Full Stack")

    choice = input("\nEnter choice: ").strip()

    interview_types = {
        "1": "DSA",
        "2": "Backend",
        "3": "Python",
        "4": "AI/ML",
        "5": "Full Stack"
    }

    if choice not in interview_types:
        print("\n❌ Invalid choice. Please select 1-5.")
        return

    interview_type = interview_types[choice]
    print(f"\n✅ Selected Interview Type: {interview_type}")

    question_count = 0
    results = []
    
    conversation_history = [
        SystemMessage(
            content=(
                "You are an expert technical interviewer. "
                "You are conducting a professional technical interview. "
                "Ask concise and technically accurate questions. "
                "Do not reveal answers before the candidate responds."
            )
        )
    ]

    try:
        question = generate_first_question(interview_type, conversation_history)

        while question_count < MAX_QUESTIONS:
            question_count += 1

            print("\n========================================")
            print(f"             QUESTION {question_count}")
            print("========================================")
            print(f"\n{question}")

            print("\nYour Answer:")
            answer = input("> ").strip()

            if not answer:
                print("\n❌ Answer cannot be empty.")
                question_count -= 1
                continue

            conversation_history.append(HumanMessage(content=answer))

            print("\n⏳ Evaluating your answer...")
            feedback = evaluate_answer(
                interview_type=interview_type,
                question=question,
                answer=answer
            )

            conversation_history.append(
                AIMessage(
                    content=(
                        f"Score: {feedback.score}/10\n"
                        f"Correct: {feedback.correct}\n"
                        f"Strengths: {', '.join(feedback.strengths)}\n"
                        f"Weaknesses: {', '.join(feedback.weaknesses)}\n"
                        f"Improvement: {feedback.improvement}"
                    )
                )
            )

            results.append({
                "question": question,
                "answer": answer,
                "score": feedback.score,
                "correct": feedback.correct,
                "strengths": feedback.strengths,
                "weaknesses": feedback.weaknesses,
                "improvement": feedback.improvement
            })

            display_feedback(feedback)

            if feedback.next_action == "finish":
                print("\n🛑 Interview finished by AI.")
                break

            if question_count >= MAX_QUESTIONS:
                print("\n🛑 Maximum questions reached.")
                break

            question = generate_next_question(
                interview_type=interview_type,
                conversation_history=conversation_history,
                previous_feedback=feedback
            )
            
            conversation_history.append(AIMessage(content=question))

    except KeyboardInterrupt:
        print("\n\nInterview stopped by user.")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

    # Final Report
    print("\n\n========================================")
    print("          FINAL INTERVIEW REPORT")
    print("========================================")

    if not results:
        print("\nNo questions were completed.")
        return

    total_score = sum(result["score"] for result in results)
    average_score = total_score / len(results)

    print(f"\nQuestions Attempted: {len(results)}")
    print(f"Average Score: {average_score:.1f}/10")

    if average_score >= 8:
        performance = "Excellent"
    elif average_score >= 6:
        performance = "Good"
    elif average_score >= 4:
        performance = "Needs Improvement"
    else:
        performance = "Needs Significant Improvement"

    print(f"Performance: {performance}")
    print("\nScore Breakdown:")

    for index, result in enumerate(results, start=1):
        print(f"Question {index}: {result['score']}/10")

    all_strengths = []
    all_weaknesses = []

    for result in results:
        all_strengths.extend(result["strengths"])
        all_weaknesses.extend(result["weaknesses"])

    print("\nStrong Areas:")
    for strength in all_strengths:
        print(f"  ✓ {strength}")

    print("\nAreas to Improve:")
    for weakness in all_weaknesses:
        print(f"  ✗ {weakness}")

    if average_score >= 8:
        recommendation = (
            "Your fundamentals are strong. "
            "Focus on advanced interview questions "
            "and system-level problem solving."
        )
    elif average_score >= 6:
        recommendation = (
            "Your fundamentals are good. "
            "Practice more questions and improve "
            "the depth of your technical explanations."
        )
    else:
        recommendation = (
            "Focus on strengthening your fundamentals "
            "and practice basic questions before "
            "moving to advanced topics."
        )

    print("\nOverall Recommendation:")
    print(recommendation)
    print("\n========================================")
    print("       INTERVIEW COMPLETED")
    print("========================================")

if __name__ == "__main__":
    main()