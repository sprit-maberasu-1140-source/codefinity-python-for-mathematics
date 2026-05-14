import random

def estimate_pi(num_points):
    points_inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            points_inside_circle += 1
    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate

num_points = 10000
pi_approximation = estimate_pi(num_points)
print("Estimated value of pi:", pi_approximation)