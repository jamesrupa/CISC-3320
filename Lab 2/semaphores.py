import os
import random
import time
from threading import *

# global variables --> computer resources
PRINTERS = 5
PLOTTERS = 6
SCANNERS = 4

# initialize semaphores
printer = Semaphore(PRINTERS)
plotter = Semaphore(PLOTTERS)
scanner = Semaphore(SCANNERS)

# random number picking which resource to pick
# 1 = printer
# 2 = plotter
# 3 = scanner
def randomRequest():
    return random.randint(1, 3)

# prints the requested resource type
def computerResource(numID):
    if numID == 1:
        print('Resource: Printer')
    elif numID == 2:
        print('Resource: Plotter')
    else:
        print('Resource: Scanner')

# request the resource if avaliable
def task(numID):
    if numID == 1:
        return printer
    elif numID == 2:
        return plotter
    else:
        return scanner

# routine, sequences 4 times
for i in range(4):
    process = os.fork()
    if process == 0:
        # this is child process
        resource = randomRequest()
        semaphoreRequest = computerResource(resource)
        while semaphoreRequest == 0:
            # unable to get resource
            # wait
            waitTime = random.randint(2, 5)
            time.sleep(waitTime)
            # attempts to request after waiting
            semaphoreRequest = computerResource(resource)
            print('Unable to request resource')
        # able to grab resource
        acqTask = task(resource)
        acqTask.acquire()
        print('Sucessful --> able to request', os.getpid())
        waitTime = random.randint(1, 4)
        time.sleep(waitTime)

        # releases and terminates
        acqTask.release()
        os._exit(0)