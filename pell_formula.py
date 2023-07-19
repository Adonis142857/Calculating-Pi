import time
import math

start_time = time.time()
k = 0
pi = 0
while True:
    pi += math.pow(-1, k) / (2*k+1)
    elapsed_time = time.time() - start_time
    with open('pell_formula.txt', 'a') as f:
        f.write(f'π estimate: {4*pi}, time elapsed: {elapsed_time} seconds\n')
    k += 1
