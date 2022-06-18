import concurrent.futures
import asyncio

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

async def main(loop, executor, n):
    n_factorial = await loop.run_in_executor(executor, factorial,n)
    print('The factorial of {} is {}'.format(n, n_factorial))

if __name__ == '__main__':
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=1)
    loop = asyncio.get_event_loop()
    n = 1
    try:
        while True:
            loop.run_until_complete(main(loop, executor, n))
            n=n+1
            if n > 25:
                break
    finally:
        loop.close()

