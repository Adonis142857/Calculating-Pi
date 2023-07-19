import time
import math

start_time = time.time()
a = 1
b = 1 / math.sqrt(2)
t = 1 / 4
p = 1

while True:
    a_next = (a + b) / 2
    b = math.sqrt(a * b)
    t -= p * (a - a_next)**2
    a = a_next
    p *= 2

    pi_estimate = (a + b)**2 / (4 * t)
    elapsed_time = time.time() - start_time

    with open('gauss_legendre.txt', 'a') as f:
        f.write(f'π estimate: {pi_estimate}, time elapsed: {elapsed_time} seconds\n')
