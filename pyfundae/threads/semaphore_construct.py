"""
Parallel computing benefits:
High Performance, Better use of resources, fairness, convenience, Fault Tolerance

Challenges:
race conditions - two concurrent instruction sequences access the same address in memory , and atleast one of them
                  writes to that address

starvation, deadlock, livelock
"""

import threading


class Semaphore:
    def __init__(self, max_available):
        self.cv = threading.Condition()
        self.MAX_AVAILABLE = max_available
        self.taken = 0

    def acquire(self):
        self.cv.acquire()
        while self.cv == self.MAX_AVAILABLE:
            self.cv.wait()
        self.taken += 1
        self.cv.release()

    def release(self):
        self.cv.acquire()
        self.taken -= 1
        self.cv.notify()
        self.cv.release()
