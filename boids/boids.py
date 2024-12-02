"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

import random

boid_x_positions=[random.uniform(-450,50.0) for x in range(50)]
boid_y_positions=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boid_x_positions,boid_y_positions,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    boid_x_position,boid_y_position,boid_x_velocity,boid_y_velocity=boids

    # Fly towards the middle
    for i in range(len(boid_x_position)):
        for j in range(len(boid_x_position)):
            boid_x_velocity[i]=boid_x_velocity[i]+(boid_x_position[j]-boid_x_position[i])*0.01/len(boid_x_position)
    for i in range(len(boid_x_position)):
        for j in range(len(boid_x_position)):
            boid_y_velocity[i]=boid_y_velocity[i]+(boid_y_position[j]-boid_y_position[i])*0.01/len(boid_x_position)
    # Fly away from nearby boids
    for i in range(len(boid_x_position)):
        for j in range(len(boid_x_position)):
            if (boid_x_position[j]-boid_x_position[i])**2 + (boid_y_position[j]-boid_y_position[i])**2 < 100:
                boid_x_velocity[i]=boid_x_velocity[i]+(boid_x_position[i]-boid_x_position[j])
                boid_y_velocity[i]=boid_y_velocity[i]+(boid_y_position[i]-boid_y_position[j])
    # Try to match speed with nearby boids
    for i in range(len(boid_x_position)):
        for j in range(len(boid_x_position)):
            if (boid_x_position[j]-boid_x_position[i])**2 + (boid_y_position[j]-boid_y_position[i])**2 < 10000:
                boid_x_velocity[i]=boid_x_velocity[i]+(boid_x_velocity[j]-boid_x_velocity[i])*0.125/len(boid_x_position)
                boid_y_velocity[i]=boid_y_velocity[i]+(boid_y_velocity[j]-boid_y_velocity[i])*0.125/len(boid_x_position)
    # Move according to velocities
    for i in range(len(boid_x_position)):
        boid_x_position[i]=boid_x_position[i]+boid_x_velocity[i]
        boid_y_position[i]=boid_y_position[i]+boid_y_velocity[i]
