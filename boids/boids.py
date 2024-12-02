"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""
from dataclasses import dataclass

import numpy as np

@dataclass
class Boids:
    x: float
    y: float
    velocity_x: float
    velocity_y: float

def update_boids(boids_lst: list[Boids],
                 towards_middle_coefficient=0.01, fly_away_distance=100, nearby_distance=10000,
                 nearby_coefficient=0.125):
    # Fly towards the middle
    for boid in boids_lst:
        for other_boid in boids_lst:
            boid.velocity_x = boid.velocity_x + (other_boid.x- boid.x)*towards_middle_coefficient/len(boids_lst)
            boid.velocity_y = boid.velocity_y + (other_boid.y - boid.y)*towards_middle_coefficient/len(boids_lst)
    # Fly away from nearby boids
    for boid in boids_lst:
        for other_boid in boids_lst:
            if (other_boid.x - boid.x)**2 + (other_boid.y - boid.y)**2 < fly_away_distance:
                boid.velocity_x += boid.x - other_boid.x
                boid.velocity_y += boid.y - other_boid.y
    # Try to match speed with nearby boids
    for boid in boids_lst:
        for other_boid in boids_lst:
            if (other_boid.x - boid.x)**2 + (other_boid.y - boid.y)**2 < nearby_distance:
                boid.velocity_x += (other_boid.velocity_x - boid.velocity_x)*nearby_coefficient/len(boids_lst)
                boid.velocity_y += (other_boid.velocity_y - boid.velocity_y)*nearby_coefficient/len(boids_lst)
    # Move according to velocities
    for boid in boids_lst:
        boid.x += boid.velocity_x
        boid.y += boid.velocity_y

if __name__ == "__main__":
    population = 50
    boids_lst = []
    x=np.random.uniform(-450, 50., size=50)
    y=np.random.uniform(300, 600., size = 50)
    velocity_x=np.random.uniform(0, 10, size=50)
    velocity_y=np.random.uniform(-20, 20, size=50)
    for i in range(population):
        boids_lst.append(Boids(x[i], y[i], velocity_x[i], velocity_y[i]))
    update_boids(boids_lst)