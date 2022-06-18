import  aiofiles

with open('logfile.log', mode='r') as f:
    contents = f.read()

print(contents)

async with aiofiles.open('logfile.log', mode='r') as f:
    contents = f.read()

print(contents)
with open('write.log', mode='w') as f:
    f.write('data')


async with aiofiles.open('logfile.log', mode='w') as f:
    await f.write('data')

print(contents)
