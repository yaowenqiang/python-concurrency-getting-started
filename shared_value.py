from multiprocessing import Value, Lock
counter = Value('i') # shared object of type int, defaults to 0
is_running = Value(ctypes.c_bool, False, lock=False) # shared object of type boolean, defaulting is False, unsynchronized

my_lock = Lock()

size_counter = Value('i', 0, lock=my_lock) # shared object of type long, with a lock specified