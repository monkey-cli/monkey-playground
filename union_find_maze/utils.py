import numpy as np
from union_find import union, find, connected


def get_surroundings(matrix, coord):
    """
    Get surrounding coordinates only if their indexes are part of the matrix
    """
    width = np.shape(matrix)[0]
    height = np.shape(matrix)[1]
    coordinates = []

    # top
    (
        coordinates.append((coord[0], coord[1] - 1))
        if coord[1] - 1 >= 0
        else None
    )
    # bottom
    (
        coordinates.append((coord[0], coord[1] + 1))
        if coord[1] + 1 < height
        else None
    )
    # left
    (
        coordinates.append((coord[0] - 1, coord[1]))
        if coord[0] - 1 >= 0
        else None
    )
    # right
    (
        coordinates.append((coord[0] + 1, coord[1]))
        if coord[0] + 1 < width
        else None
    )

    return coordinates


def find_indexes_of_cords(coordinates, hashTable):
    indexes = []
    for item in coordinates:
        indexes.append(hashTable.index(item))
    return indexes


def get_possible_next_steps(matrix, hashTable, coordinate):
    """
    Get possible next steps indexes for the maze route.
    """
    surroundings_coordinates = get_surroundings(matrix, coordinate)
    # get only surrounding coordinates that represent an "EMPTY" /not "WALL"
    filtered_surroundings = []
    for coord in surroundings_coordinates:
        item = matrix[coord[0]][coord[1]]
        if item == 0:
            filtered_surroundings.append(coord)

    indexes = find_indexes_of_cords(filtered_surroundings, hashTable)
    return indexes


def get_non_connected_next_steps(data, currentStep, possible_next_steps):
    next_steps = []
    for step in possible_next_steps:
        if not connected(data, currentStep, step):
            next_steps.append(step)
    return next_steps
