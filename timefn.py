import time
from functools import wraps
from datetime import datetime
def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        current_time = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
        print(f"{current_time} @timefn:" + fn.__name__ + " took " + str(t2 - t1) + "seconds")
        return result
    return measure_time

class Demo():
    def __init__(self):
        pass

    @timefn
    def test(self):
        test()


@timefn
def test():
    for i in range(100000):
        print(i)

if __name__ == '__main__':
    #test()

    d = Demo()
    d.test()
