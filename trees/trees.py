"""
This code produces a tree like plot. In order to achieve this we plot an initial
line and present the roots/trunk of the tree, after which we produce a loop to
set the x and y values. This then plots the points on a graph through matplotlib
which produces a graph similar to the shape of a tree.
"""

from math import sin, cos
from matplotlib import pyplot as plt

branch_length = 1  # length of the first branch
branches = [
    [0, 1, 0]
]  # list of branches, each branch is a list of 3 numbers: x, y, angle
plt.plot([0, 0], [0, 1])  # plots the initial line of the tree
for i in range(5):
    new_branches = []
    for branch in branches:  # Loop over existing branches
        x, y, angle = branch

        # Calculate new branch points
        new_x1 = x + branch_length * sin(angle - 0.1)
        new_y1 = y + branch_length * cos(angle - 0.1)
        new_angle1 = angle - 0.1

        new_x2 = x + branch_length * sin(angle + 0.1)
        new_y2 = y + branch_length * cos(angle + 0.1)
        new_angle2 = angle + 0.1

        # Append new branches to the list
        new_branches.append([new_x1, new_y1, new_angle1])
        new_branches.append([new_x2, new_y2, new_angle2])

        # Plot the new branches
        plt.plot([x, new_x1], [y, new_y1])
        plt.plot([x, new_x2], [y, new_y2])

    branches = new_branches
    branch_length *= 0.6

plt.savefig("tree.png")
