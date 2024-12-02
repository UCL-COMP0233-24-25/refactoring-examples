"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

import random

random.seed(1)
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    boids_x,boids_y,boid_x_velocities,boid_y_velocities=boids
    
    for i in range(len(boids_x)):
        for j in range(len(boids_x)):
            # Fly towards the middle
            boid_x_velocities[i]=boid_x_velocities[i]+(boids_x[j]-boids_x[i])*0.01/len(boids_x)
            boid_y_velocities[i]=boid_y_velocities[i]+(boids_y[j]-boids_y[i])*0.01/len(boids_x)
            # Fly away from nearby boids
            if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 100:
                boid_x_velocities[i]=boid_x_velocities[i]+(boids_x[i]-boids_x[j])
                boid_y_velocities[i]=boid_y_velocities[i]+(boids_y[i]-boids_y[j])
            # Try to match speed with nearby boids
            elif (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 10000:
                boid_x_velocities[i]=boid_x_velocities[i]+(boid_x_velocities[j]-boid_x_velocities[i])*0.125/len(boids_x)
                boid_y_velocities[i]=boid_y_velocities[i]+(boid_y_velocities[j]-boid_y_velocities[i])*0.125/len(boids_x)
        # Move according to velocities
        boids_x[i]=boids_x[i]+boid_x_velocities[i]
        boids_y[i]=boids_y[i]+boid_y_velocities[i]

