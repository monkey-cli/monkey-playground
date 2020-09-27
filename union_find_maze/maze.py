import math
import numpy as np
from random import randrange
from union_find import union, find, connected
from utils import get_possible_next_steps, get_non_connected_next_steps
from mock import get_maze
"""
Task: Try to find the route in the provided maze from origin (0,0) to destination (N-1,M-1).
N-number of rows, M-number of columns.

The maze is represented as a matrix of bits, where 0 represents an empty slot and 1 represents a wall.
# 0 -> empty
# 1 -> wall
Find the connected coordinates with value of 0 that connect from start to destination.

To solve the problem we will use the Disjoint Set (Union Find) algorithm.
"""
maze = get_maze()
rows = np.shape(maze)[0]
columns = np.shape(maze)[1]
# start = maze[0][0]
# end = maze[rows-1][columns-1]

# The number of elements in this union find
size = rows * columns

if (size <= 0):
    raise Exception("Size <= 0 is not allowed")

# Step 1
# construct a bijection (a mapping) between the coordinates of the matrix and integers in range [0, n).
# this will allow an array based union find, easy to work with.
hashTable = []
# data[i] points to the parent of i, if data[i] = i then i is a root node
data = []
hashIndex = 0
for row in range(0, rows):
    for column in range(0, columns):
        hashTable.append((row, column))
        data.append(hashIndex)
        hashIndex += 1

# ------------------------------------------------------------------------


def find_next_steps(currect_index):
    """
    Helper function used to find only the acceptable next steps
    """
    matrixCoord = hashTable[currect_index]
    possible_next_steps = get_possible_next_steps(maze, hashTable, matrixCoord)
    next_steps = get_non_connected_next_steps(
        data, currect_index, possible_next_steps)

    return next_steps


def run_union_find(onStepUpdate=None):

    # ------------------------------------------------------------------------
    # start from the start of the maze and look for the next connection
    currect_index = 0  # index in the data array
    # while the start and end of the maze are not connected
    # try to find the next connected item of the path
    steps = []
    while(not connected(data, 0, size-1)):
        # for currect cell get all surrounding coordinates
        # from these coordinates randomly select one as the next step,
        # but with the condition that this coordinate is not connected to the currect cell and is not a "WALL"

        # for every loop save the steps
        steps.append(currect_index)

        next_steps = find_next_steps(currect_index)

        if len(next_steps) == 0:
            """
            Dead end reached. Need to get back and look at previous connections next steps.
            """
            print("Dead end at index:", currect_index,
                  "and coordinate:", hashTable[currect_index])
            if onStepUpdate:
                onStepUpdate(
                    {
                        "status": "DEAD_END",
                        "value": hashTable[currect_index]
                    }
                )
            prev_step = steps.index(currect_index) - 1
            while(prev_step >= 0 and len(find_next_steps(steps[prev_step])) == 0):
                # go check for a new route starting from one step before the current one
                # loop until a node with possible next steps to be folowed
                prev_step -= 1
            if (prev_step >= 0):
                print("Loogin for new route at index", steps[prev_step])
                currect_index = steps[prev_step]
                continue
            else:
                print("Could not find a route from start to end... :(")
            break

        # get a random item from the array
        next_index = next_steps[randrange(len(next_steps))]
        union(data, currect_index, next_index)
        print("Iteration at index", currect_index)
        if onStepUpdate:
            onStepUpdate(
                {
                    "status": "NEXT_STEP",
                    "value": hashTable[currect_index]
                }
            )
        # prepare for next loop
        currect_index = next_index

    print("Iteration at last index", size-1)
    print("--------------------------------------------------------")
    # append last index of the array
    steps.append(size-1)

    step_coordinates = list(map(lambda item: hashTable[item], steps))
    print("Iteration traversed the following coordinates:")
    print(step_coordinates)
