import time
import os

def illuminate(source, idx=0):
    output = (" " * idx) + source[idx]
    print(output)

    return

def spotlight(source, delay=.25, reverse=False):
    iter = None
    if reverse:
        iter = range(len(source) - 1, -1, -1)
    else:
        iter = range(0, len(source), 1)

    for i in iter:
        os.system('clear')
        illuminate(source, i)
        time.sleep(delay)

def sweep(source, delay=.25, iters=10):
    for iter in range(iters):
        spotlight(source, delay)
        spotlight(source, delay, True)

if __name__ == '__main__':
    sweep("Hollywood")
