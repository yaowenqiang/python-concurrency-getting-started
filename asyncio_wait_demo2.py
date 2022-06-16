import asyncio


async def get_item(i):
    await asyncio.sleep(i)
    return 'item ' + str(i)


async def get_items(num_items):
    print('getting items')
    item_coros = [
        get_item(i)
        for i in range(num_items)
    ]
    print('waiting 2 seconds for tasks to complete')
    completed, pending = await asyncio.wait(item_coros, timeout=2)
    results = [t.result() for t in completed]
    print('results: {!r}'.format(results))

    if pending:
        print('canceling remaining tasks')
        for t in pending:
            t.cancel()


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(get_items(4))
finally:
    loop.close()
