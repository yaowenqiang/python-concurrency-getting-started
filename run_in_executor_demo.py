import asyncio
import concurrent.futures
import time


def blocking_func(n):
    time.sleep(0.5)
    return n ** 2


async def main(loop, executor):
    print('creating executor tasks')
    blocking_tasks = [
        loop.run_in_executor(executor, blocking_func, i)
        for i in range(6)
    ]
    print('waiting for tasks to complete')

    results = await asyncio.gather(*blocking_tasks)
    print('results: {!r}'.format(results))

if __name__ == '__main__':
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop, executor))
    finally:
        loop.close()