#!/usr/bin/env python3
from multiprocessing import Process
import time
import os


def sleep(n: float):
    print("start process: %d" % os.getpid())
    time.sleep(10)


def start():
    now = time.time()
    processes = []
    for _ in range(0,10):
        p = Process(target=sleep, args=(5,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    print("Total cost %.2f seconds" % (time.time()-now))


if __name__ == "__main__":
    start()
