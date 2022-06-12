import random
from multiprocessing import Process, Pipe
def make_tuple(conn):
    num = random.randint(1,9)
    conn.send(('Hi ', num))
    print(conn.recv())


def make_string(conn):
    tup = conn.recv()
    result = ''
    substr, num = tup
    for _ in range(num):
        result += substr
    conn.send(result)

if __name__ == '__main__':
    conn1, conn2 = Pipe(True)
    p1 = Process(target=make_tuple, args=(conn1,))
    p2 = Process(target=make_string, args=(conn2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
