from threading import Thread
from queue import Queue

def producer(queue):
    for i in range(10):
        item = make_an_item_available()
        queue.put(item)

    queue.put(0)

def consumer(queue):
    while True:
        item = queue.get() # if queue is empty ,the get call will block
        if item == 0:
            # poison pill
            queue.task_done()
            break
        item = queue.get(block=False) # with the block=False flag, get call won't be blocked
        # do something with the item
        print(item)
        queue.task_done()


def make_an_item_available():
    return 1
queue = Queue()
t1 = Thread(target=producer, args=(queue,))
t2 = Thread(target=consumer, args=(queue,))

t1.start()
t2.start()

t1.join()
t2.join()

