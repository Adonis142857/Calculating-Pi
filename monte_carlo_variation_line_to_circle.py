import random
import time

start_time = time.time()

total_lines = 0
intersect_lines = 0

while True:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    angle = random.uniform(0, 180)
    if abs(y - x * angle) < 1:
        intersect_lines += 1
    total_lines += 1

    pi_estimate = 2 * total_lines / intersect_lines
    elapsed_time = time.time() - start_time

    with open('monte_carlo_variation_line_to_circle.txt', 'a') as f:
        f.write(f'π estimate: {pi_estimate}, time elapsed: {elapsed_time} seconds\n')
