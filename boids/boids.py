"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids, middle_param=0.01, nearby_away = 100, nearby_match_speed = 10000):
    x_positions,y_positions,x_velocities,y_velocities=boids
    
    # Fly towards the middle
    for i in x_positions:
        for j in x_positions:
            x_velocities[i]=x_velocities[i]+(x_positions[j]-x_positions[i])*middle_param/len(x_positions)
            y_velocities[i]=y_velocities[i]+(y_positions[j]-y_positions[i])*middle_param/len(x_positions)
    # Fly away from nearby boids      
            if (x_positions[j]-x_positions[i])**2 + (y_positions[j]-y_positions[i])**2 < nearby_away:
                x_velocities[i]=x_velocities[i]+(x_positions[i]-x_positions[j])
                y_velocities[i]=y_velocities[i]+(y_positions[i]-y_positions[j])
    # Try to match speed with nearby boids
            if (x_positions[j]-x_positions[i])**2 + (y_positions[j]-y_positions[i])**2 < nearby_match_speed:
                x_velocities[i]=x_velocities[i]+(x_velocities[j]-x_velocities[i])*0.125/len(x_positions)
                y_velocities[i]=y_velocities[i]+(y_velocities[j]-y_velocities[i])*0.125/len(x_positions)
    # Move according to velocities
        x_positions[i]=x_positions[i]+x_velocities[i]
        y_positions[i]=y_positions[i]+y_velocities[i]
