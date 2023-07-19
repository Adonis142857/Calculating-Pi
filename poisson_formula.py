import time
import math

start_time = time.time()
n = 0
pi_estimate = 0

while True:
    pi_estimate += math.sqrt(1 - (n / 1000)**2) / 1000
    pi_estimate *= 4
    elapsed_time = time.time() - start_time

    with open('poisson_formula.txt', 'a') as f:
        f.write(f'π estimate: {pi_estimate}, time elapsed: {elapsed_time} seconds\n')
    n += 1
