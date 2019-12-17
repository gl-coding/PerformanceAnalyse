import multiprocessing
import time
import random
import sys

def worker1(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        intv = random.randint(0,3)
        print "randint value is : %s" % intv
        res = intv%2
        sys.exit(1)
        n -= 1

if __name__ == "__main__":
    worker = []
    for i in range(0, 1):
        worker.append(multiprocessing.Process(target = worker1, args = (3,)))
    for i in range(0, 1):
        worker[i].start()
    for i in range(0, 1):
        worker[i].join()
    
    print worker[i].exitcode
    print "finish"