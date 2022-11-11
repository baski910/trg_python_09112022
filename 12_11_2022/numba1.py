import random
import time
from numba import njit

@njit
def pi(npoints):
    n_in_circle = 0
    for i in range(npoints):
        x = random.random()
        y = random.random()

        if ((x**2+y**2)< 1):
            n_in_circle += 1
    return 4*n_in_circle/npoints

if __name__ == '__main__':
    t1 = time.time()
    pi(10000000)
    t2 = time.time()
    t = t2-t1
    print(t)
