import asyncio


# --------------------------------
# Research Agent
# --------------------------------

async def research_agent():

    print("Research Agent started")

    await asyncio.sleep(3)

    print("Research Agent completed")

    return "Research data"


# --------------------------------
# News Agent
# --------------------------------

async def news_agent():

    print("News Agent started")

    await asyncio.sleep(2)

    print("News Agent completed")

    return "News data"


# --------------------------------
# Documentation Agent
# --------------------------------

async def docs_agent():

    print("Docs Agent started")

    await asyncio.sleep(1)

    print("Docs Agent completed")

    return "Documentation data"


# --------------------------------
# Main
# --------------------------------

async def main():

    print("Multi-agent research started\n")

    results = await asyncio.gather(
        research_agent(),
        news_agent(),
        docs_agent()
    )

    print("\nAll agents completed")

    print("\nResults:")
    print(results)


# --------------------------------
# Start Program
# --------------------------------

asyncio.run(main())