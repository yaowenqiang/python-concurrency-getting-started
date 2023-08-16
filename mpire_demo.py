import time
from multiprocessing import Pool
from mpire import WorkerPool

def time_consuming_function(x):
    time.sleep(1)
    return 

with Pool(processes=5) as pool:
    results = pool.map(time_consuming_function, range(10))

with WorkerPool(n_jobs=5) as pool:
    results = pool.map(time_consuming_function, range(10), progress_bar=True)
