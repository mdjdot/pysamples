#!/usr/bin/env python
from threading import Thread
from threading import Lock

import time
import os

lock = Lock()

def sleep(n: float):
    lock.acquire()
    print("start thread: %d" % os.getpid())
    lock.release()
    time.sleep(10)

def start():
    now = time.time()
    threads = []
    for _ in range(0,10):
        t = Thread(target=sleep, args=(5,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print("Total cost %.2f seconds" % (time.time()-now))


if __name__ == "__main__":
    start()