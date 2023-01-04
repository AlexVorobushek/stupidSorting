from multiprocessing import Process
import time


def pr_func(item, start_time):
    while time.time() < start_time:
        pass
    time.sleep(item*0.1)
    print(item)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 10, 12, 3, 41, 40, 2, 0]
    start_time = time.time() + 2
    
    prs = [Process(target=pr_func, args=(item, start_time)) for item in data]
    for pr in prs:
        pr.start()
    for pr in prs:
        pr.join()
    print('Done.')
