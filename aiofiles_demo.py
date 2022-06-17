import  aiofiles

with open('logfile.log', mode='r') as f:
    contents = f.read()

print(contents)

async with aiofiles.open('logfile.log', mode='r') as f:
    contents = f.read()

print(contents)
