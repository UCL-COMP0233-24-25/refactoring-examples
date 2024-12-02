from math import sin, cos
from matplotlib import pyplot as plt

# Constants
BRANCH_ANGLE = 0.1  # Angle offset for branches
ITERATIONS = 5      # Number of iterations for tree depth
INITIAL_LENGTH = 1  # Initial branch length
LENGTH_DECAY = 0.6  # Decay rate for branch length

def generate_tree(branches, segment_length, angle_offset):
    """
    Generate new branches for each iteration.

    Parameters:
    branches: list, current list of branches, each branch is [x, y, angle]
    segment_length: float, current branch length
    angle_offset: float, angle offset for branches

    Returns:
    new_branches: list, list of newly generated branches
    """
    new_branches = []
    for branch in branches:
        x, y, angle = branch
        # Calculate left branch
        left_branch = [
            x + segment_length * sin(angle - angle_offset), 
            y + segment_length * cos(angle - angle_offset), 
            angle - angle_offset
        ]
        # Calculate right branch
        right_branch = [
            x + segment_length * sin(angle + angle_offset), 
            y + segment_length * cos(angle + angle_offset), 
            angle + angle_offset
        ]
        # Add branches to the list
        new_branches.extend([left_branch, right_branch])
        # Plot branches
        plt.plot([x, left_branch[0]], [y, left_branch[1]], color='green')
        plt.plot([x, right_branch[0]], [y, right_branch[1]], color='green')
    return new_branches

def plot_tree():
    """
    Plot the tree-like structure.
    """
    # Initialize the root branch
    branches = [[0, 0, 0]]  # Root branch format: [x, y, angle]
    segment_length = INITIAL_LENGTH  # Initial branch length
    
    # Set up the figure
    plt.figure(figsize=(8, 8))
    # Draw the trunk
    plt.plot([0, 0], [0, 1], color='brown')
    
    # Generate branches iteratively
    for _ in range(ITERATIONS):
        branches = generate_tree(branches, segment_length, BRANCH_ANGLE)
        segment_length *= LENGTH_DECAY  # Decrease the length for the next iteration
    
    # Remove axes
    plt.axis('off')
    # Save the resulting plot
    plt.savefig('tree.png', dpi=300)
    # Close the plot to free resources
    plt.close()

# Call the function to draw and save the tree
plot_tree()


