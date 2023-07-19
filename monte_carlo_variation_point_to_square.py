import random
import time
import math

start_time = time.time()
inside_circle = 0
total_points = 0
while True:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = math.sqrt(x**2 + y**2)
    if distance <= math.sqrt(2):
        inside_circle += 1
    total_points += 1
    pi_estimate = 4 * inside_circle / total_points
    elapsed_time = time.time() - start_time
    with open('monte_carlo_variation_point_to_square.txt', 'a') as f:
        f.write(f'π estimate: {pi_estimate}, time elapsed: {elapsed_time} seconds\n')
