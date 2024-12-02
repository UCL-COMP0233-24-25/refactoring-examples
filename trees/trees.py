"""This code produces a tree-like plot through matplotlib."""

from math import sin, cos
from matplotlib import pyplot as plt

def tree(branch_length=1, angle=0.1):
    branch_length = 1  # length of the first branch
    branches = [
        [0, 1, 0]
    ]  # list of branches, each branch is a list of 3 numbers: x, y, angle
    plt.plot([0, 0], [0, branch_length])  # 
    for i in range(5):
        new_branches = []
        for x, y, angle in branches:  # Loop over existing branches

            # Calculate new branch points
            new_x1 = x + branch_length * sin(angle - angle)
            new_y1 = y + branch_length * cos(angle - angle)
            new_angle1 = angle - angle

            new_x2 = x + branch_length * sin(angle + angle)
            new_y2 = y + branch_length * cos(angle + angle)
            new_angle2 = angle + angle

            # Append new branches to the list
            new_branches.append([new_x1, new_y1, new_angle1])
            new_branches.append([new_x2, new_y2, new_angle2])

            # Plot the new branches
            plt.plot([x, new_x1], [y, new_y1])
            plt.plot([x, new_x2], [y, new_y2])
            
        branches = new_branches
        branch_length *= 0.6

if __name__ == "__main__":
    tree()
    plt.savefig("tree.png")
