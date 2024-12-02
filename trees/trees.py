"""This code produces a tree-like plot through matplotlib."""

from math import sin, cos
from matplotlib import pyplot as plt

branch_length = 1  # length of the first branch
branches = [
    [0, 1, 0]
]  # list of branches, each branch is a list of 3 numbers: x, y, angle
plt.plot([0, 0], [0, 1])  #
for i in range(5):
    new_branches = []
    for j in range(len(branches)):  # loop over d
        new_branches.append(
            [
                branches[j][0] + branch_length * sin(branches[j][2] - 0.1),
                branches[j][1] + branch_length * cos(branches[j][2] - 0.1),
                branches[j][2] - 0.1,
            ]
        )
        new_branches.append(
            [
                branches[j][0] + branch_length * sin(branches[j][2] + 0.1),
                branches[j][1] + branch_length * cos(branches[j][2] + 0.1),
                branches[j][2] + 0.1,
            ]
        )
        plt.plot(
            [branches[j][0], new_branches[-2][0]], [branches[j][1], new_branches[-2][1]]
        )
        plt.plot(
            [branches[j][0], new_branches[-1][0]], [branches[j][1], new_branches[-1][1]]
        )
    d = new_branches
    branch_length *= 0.6
plt.savefig("tree.png")
