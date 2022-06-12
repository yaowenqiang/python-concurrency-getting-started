import multiprocessing
import time

def do_work():
    print('Start do_work function')
    # print(f'echo {val}')
    time.sleep(5)
    print('Finished do_work function')

if __name__ == '__main__':
    # val = 'text'
    # vargs value must be picklable
    p = multiprocessing.Process(target=do_work)
    print('[Before start] Process is alive: {}'.format(p.is_alive()))
    p.start()
    print('[Running] Process is alive: {}'.format(p.is_alive()))
    p.terminate()
    p.join()
    print('[After Terminating] Process is alive: {}'.format(p.is_alive()))
    print('Process exit code: {}'.format(p.exitcode))
