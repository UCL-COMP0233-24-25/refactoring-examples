from math import sin, cos
from matplotlib import pyplot as plt


def tree(branch_length=1, branch_angle=0.1, num_branches=5):
    """
    This function produces a tree like plot. In order to achieve this we plot an initial
    line and present the roots/trunk of the tree, after which we produce a loop to
    set the x and y values. This then plots the points on a graph through matplotlib
    which produces a graph similar to the shape of a tree.

    Parameters:
        branch_length (float): The length of the branches of the tree.
        branch_angle (float): The angle between the branches of the tree.
        num_branches (int): The number of branches the tree has.
    """
    branches = [
        [0, 1, 0]
    ]  # list of branches, each branch is a list of 3 numbers: x, y, angle
    plt.plot([0, 0], [0, 1])  # plot the trunk of the tree
    for _ in range(num_branches):
        new_branches = []  # Create a new list of branches
        for branch in branches:
            x, y, angle = branch
            for new_angle in [angle - branch_angle, angle + branch_angle]:
                new_x = x + branch_length * sin(new_angle)
                new_y = y + branch_length * cos(new_angle)
                new_branches.append([new_x, new_y, new_angle])
                plt.plot([x, new_x], [y, new_y])

        branches = new_branches
        branch_length *= 0.6


if __name__ == "__main__":
    tree()
    plt.savefig("tree.png")
