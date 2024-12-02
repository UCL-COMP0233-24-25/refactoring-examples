"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt


def compute_coordinate(coord, length, left=True):
    """calculate the coordinate

    Args:
        coord (list): current coordinate store x, y and angle
        length (float): length of line at this level
        left (bool, optional): calculate the coordinate and angle according to the left branch or right branch. Defaults to True.

    Returns:
        list: next coordinate
    """
    angle_dif = -0.1 if left else 0.1

    next_coord_x = coord[0] + length * sin(coord[2] + angle_dif)
    next_coord_y = coord[1] + length * cos(coord[2] + angle_dif)
    next_coord_angle = coord[2] + angle_dif

    return [next_coord_x, next_coord_y, next_coord_angle]


def calculate_next_cordinates(coordinate, length):
    """caculate coordinates and length

    Args:
        coordinate (list): current coordinate store x, y and angle
        length (float): length of line at this level

    Returns:
        _type_: next coordinate, next length
    """
    next_cordinates = []
    for coord in coordinate:  # loop over coordinate
        next_cordinates.append(compute_coordinate(coord, length, True))
        next_cordinates.append(compute_coordinate(coord, length, False))
        plt.plot(
            [coord[0], next_cordinates[-2][0]],
            [coord[1], next_cordinates[-2][1]],
        )
        plt.plot(
            [coord[0], next_cordinates[-1][0]],
            [coord[1], next_cordinates[-1][1]],
        )
    coordinate = next_cordinates
    length *= 0.6

    return coordinate, length


length = 1
#  (0: x, 1 :y, 0: angle )
coordinate = [[0, 1, 0]]
plt.plot([0, 0], [0, 1])

for i in range(5):
    coordinate, length = calculate_next_cordinates(coordinate, length)

plt.savefig("tree.png")
