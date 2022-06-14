import multiprocessing

def do_work(dictionary, item):
    dictionary[item] = item ** 2


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
        multiprocessing.Process(target=do_work, args=(d,i))
        for i in range(8)
    ]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print('Results:', d)