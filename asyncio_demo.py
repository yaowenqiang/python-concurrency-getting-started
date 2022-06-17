import asyncio

async def say_hello():
    print("Hello World")

loop = asyncio.get_event_loop()
loop.run_until_complete(say_hello())
loop.close()