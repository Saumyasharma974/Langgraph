# ==========================================
# Simple Retry Strategy
# ==========================================

max_attempts = 3

for attempt in range(1, max_attempts + 1):

    print(f"\nAttempt {attempt}")

    try:
        # Simulating an operation that may fail

        if attempt < 3:
            raise Exception("Temporary error")

        print("Operation successful!")
        break

    except Exception as e:

        print(f"Operation failed: {e}")

        if attempt == max_attempts:
            print("Maximum attempts reached. Operation failed permanently.")