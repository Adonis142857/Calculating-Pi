import time
import math

start_time = time.time()
pi_estimate = 0
n = 0

while True:
    pi_estimate += (-1)**n / (2*n + 1)
    pi_estimate *= 4
    elapsed_time = time.time() - start_time

    with open('taylor_series.txt', 'a') as f:
        f.write(f'π estimate: {pi_estimate}, time elapsed: {elapsed_time} seconds\n')
    n += 1
