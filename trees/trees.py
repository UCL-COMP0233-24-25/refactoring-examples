"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt

# Defines the length of the current branch
length_increment = 1

# Offsets all the layers as a whole from the initial branch:
# x-axis: shifts the layers bundle left if -ve or right if +ve
# y-axis: shifts the layers bundle up if -ve or down if +ve
# angle: clockwise is positive, anti-clockwise is negative
layer_offset = [[0, 1, 0]]

plt.plot([0, 0], [0, 1])  # The root(beginning) of the tree
for i in range(5):  # Decide the layer numbers of the tree
    layer_storage = []
    for j in range(len(layer_offset)):
        layer_storage.append(
            [
                # Decide the x-value of the endpoint of left most branch for each layer
                layer_offset[j][0] + length_increment * sin(layer_offset[j][2] - 0.1),
                # Decide the y-value of the endpoint of left most branch for each layer
                layer_offset[j][1] + length_increment * cos(layer_offset[j][2] - 0.1),
                # Decide the angle of the left most branch for each layer
                layer_offset[j][2] - 0.1,
            ]
        )
        # Add a branch to the left

        layer_storage.append(
            [
                # Decide the x-value of the endpoint of right most branch for each layer
                layer_offset[j][0] + length_increment * sin(layer_offset[j][2] + 0.1),
                # Decide the y-value of the endpoint of right most branch for each layer
                layer_offset[j][1] + length_increment * cos(layer_offset[j][2] + 0.1),
                # Decide the angle of the right most branch for each layer
                layer_offset[j][2] + 0.1,
            ]
        )
        # Add a branch to the right

        # plot the left new branch
        plt.plot(
            [layer_offset[j][0], layer_storage[-2][0]],
            [layer_offset[j][1], layer_storage[-2][1]],
        )
        # plot the right new branch
        plt.plot(
            [layer_offset[j][0], layer_storage[-1][0]],
            [layer_offset[j][1], layer_storage[-1][1]],
        )
    layer_offset = layer_storage  # Update the layer_offset
    length_increment *= 0.6  # The offset on y axis of the endpoints of the new branch(cumulative product)
plt.savefig("tree.png")
