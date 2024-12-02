"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

import numpy as np

def update_boids(boids_x,boids_y,boid_x_velocities,boid_y_velocities):
    # Fly towards the middle
    for i in range(len(boids_x)):
        for j in range(len(boids_x)):
            boid_x_velocities[i]=boid_x_velocities[i]+(boids_x[j]-boids_x[i])*0.01/len(boids_x)
    for i in range(len(boids_x)):
        for j in range(len(boids_x)):
            boid_y_velocities[i]=boid_y_velocities[i]+(boids_y[j]-boids_y[i])*0.01/len(boids_x)
    # Fly away from nearby boids
    for i in range(len(boids_x)):
        for j in range(len(boids_x)):
            if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 100:
                boid_x_velocities[i]=boid_x_velocities[i]+(boids_x[i]-boids_x[j])
                boid_y_velocities[i]=boid_y_velocities[i]+(boids_y[i]-boids_y[j])
    # Try to match speed with nearby boids
    for i in range(len(boids_x)):
        for j in range(len(boids_x)):
            if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 10000:
                boid_x_velocities[i]=boid_x_velocities[i]+(boid_x_velocities[j]-boid_x_velocities[i])*0.125/len(boids_x)
                boid_y_velocities[i]=boid_y_velocities[i]+(boid_y_velocities[j]-boid_y_velocities[i])*0.125/len(boids_x)
    # Move according to velocities
    for i in range(len(boids_x)):
        boids_x[i]=boids_x[i]+boid_x_velocities[i]
        boids_y[i]=boids_y[i]+boid_y_velocities[i]

if __name__ == "__main__":
    boids_x=np.random.uniform(-450, 50., size=50)
    boids_y=np.random.uniform(300, 600., size = 50)
    boid_x_velocities=np.random.uniform(0,10, size=50)
    boid_y_velocities=np.random.uniform(-20,20,size=50)
    update_boids(boids_x,boids_y,boid_x_velocities,boid_y_velocities)