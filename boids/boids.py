"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

import random

num_boids = 50  
boids_x = [random.uniform(-450, 50.0) for _ in range(num_boids)]  
boids_y = [random.uniform(300.0, 600.0) for _ in range(num_boids)]  
boid_x_velocities = [random.uniform(0, 10.0) for _ in range(num_boids)]  
boid_y_velocities = [random.uniform(-20.0, 20.0) for _ in range(num_boids)]  
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)  

def update_boids(boids):  
    positions_x, positions_y, velocities_x, velocities_y = boids  
    num_boids = len(positions_x)  
    
    for i in range(num_boids):  
        center_of_mass_x = sum(positions_x) / num_boids  
        center_of_mass_y = sum(positions_y) / num_boids  
        
        # Fly towards the middle (cohesion)  
        velocities_x[i] += (center_of_mass_x - positions_x[i]) * 0.01 / num_boids  
        velocities_y[i] += (center_of_mass_y - positions_y[i]) * 0.01 / num_boids  
        
        for j in range(num_boids):  
            if i != j:  
                distance_squared = (positions_x[j] - positions_x[i])**2 + (positions_y[j] - positions_y[i])**2  
                
                # Fly away from nearby boids (separation)  
                if distance_squared < 100:  
                    velocities_x[i] += (positions_x[i] - positions_x[j])  
                    velocities_y[i] += (positions_y[i] - positions_y[j])  
                
                # Try to match speed with nearby boids (alignment)  
                if distance_squared < 10000:  
                    velocities_x[i] += (velocities_x[j] - velocities_x[i]) * 0.125 / num_boids  
                    velocities_y[i] += (velocities_y[j] - velocities_y[i]) * 0.125 / num_boids  

    # Move according to velocities  
    for i in range(num_boids):  
        positions_x[i] += velocities_x[i]  
        positions_y[i] += velocities_y[i] 