import asyncio


# ==========================================
# Long Running Task
# ==========================================

async def long_task():
    print("Task started...")

    # Simulating a task that takes 10 seconds
    await asyncio.sleep(10)

    return "Task completed"


# ==========================================
# Main Function
# ==========================================

async def main():

    try:
        result = await asyncio.wait_for(
            long_task(),
            timeout=5
        )

        print("Result:", result)

    except asyncio.TimeoutError:
        print("Task timed out!")


# ==========================================
# Run Program
# ==========================================

asyncio.run(main())