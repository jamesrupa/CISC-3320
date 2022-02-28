import os

# create first child
# creates second child, first child creates grandchild
child = os.fork()
grandchild = os.fork()

def processes():
    # parent
    if child > 0 and grandchild > 0:
        print("I am the grandparent process\nID: %d" % (os.getpid()))

    # child
    elif child == 0 and grandchild > 0:
        print("I am the parent process\nID: %d" % (os.getpid()))

    # grandchild
    elif child > 0 and grandchild == 0:
        print("I am a grandchild process\nID: %d" % (os.getpid()))

processes()