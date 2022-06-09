import threading

semaphore = threading.Semaphore()

semaphore.acquire() # decrements the counter
# access the shared resource
semaphore.release() # increments the counter