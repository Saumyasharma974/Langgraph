import asyncio
import time


async def research_task():
    await asyncio.sleep(2)
    return "Research completed"


async def news_task():
    await asyncio.sleep(5)
    return "News completed"


async def main():
    results = await asyncio.gather(
        research_task(),
        news_task()
    )
    return results


start_time = time.perf_counter()

results = asyncio.run(main())

end_time = time.perf_counter()

execution_time = end_time - start_time

print("Results:", results)
print(f"Execution time: {execution_time:.2f} seconds")