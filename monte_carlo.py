import random
import time

start_time = time.time()
inside_circle = 0
total_points = 0
while True:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = x**2 + y**2
    if distance <= 1:
        inside_circle += 1
    total_points += 1
    pi_estimate = 4 * inside_circle / total_points
    elapsed_time = time.time() - start_time
    with open('monte_carlo.txt', 'a') as f:
        f.write(f'π estimate: {pi_estimate}, time elapsed: {elapsed_time} seconds\n')
