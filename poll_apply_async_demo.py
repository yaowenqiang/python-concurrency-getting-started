from multiprocessing import Pool
import time

def multiply(x,y):
    return x * y

if __name__ == '__main__':
    pool = Pool(processes=4)
    result = pool.apply_async(multiply, (7,7)) # evaludate 'multiply(7,7)'
    print(result.get())