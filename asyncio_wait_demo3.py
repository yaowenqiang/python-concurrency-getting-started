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
    print('waiting for tasks to complete')
    results = await asyncio.gather(*item_coros)
    print('results: {!r}'.format(results))

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(get_items(4))
finally:
    loop.close()
