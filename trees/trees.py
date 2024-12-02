"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt

length = 1
#  (0: x, 1 :y, 0: angle )
coordinate = [[0, 1, 0]]
plt.plot([0, 0], [0, 1])
for i in range(5):
    next_cordinates = []
    for j in range(len(coordinate)):  # loop over d
        next_cordinates.append(
            [
                coordinate[j][0] + length * sin(coordinate[j][2] - 0.1),
                coordinate[j][1] + length * cos(coordinate[j][2] - 0.1),
                coordinate[j][2] - 0.1,
            ]
        )
        next_cordinates.append(
            [
                coordinate[j][0] + length * sin(coordinate[j][2] + 0.1),
                coordinate[j][1] + length * cos(coordinate[j][2] + 0.1),
                coordinate[j][2] + 0.1,
            ]
        )
        plt.plot(
            [coordinate[j][0], next_cordinates[-2][0]],
            [coordinate[j][1], next_cordinates[-2][1]],
        )
        plt.plot(
            [coordinate[j][0], next_cordinates[-1][0]],
            [coordinate[j][1], next_cordinates[-1][1]],
        )
    coordinate = next_cordinates
    length *= 0.6
plt.savefig("tree.png")
