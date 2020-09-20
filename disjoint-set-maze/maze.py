import math
import numpy as np


"""
Task: Try to find the route in the provided maze from origin (0,0) to destination (N-1,M-1).
N-number of rows, M-number of columns.

The maze is represented as a matrix of bits, where 0 represents an empty slot and 1 represents a wall.
# 0 -> empty
# 1 -> wall
Find the connected coordinates with value of 0 that connect from start to destination.

To solve the problem we will use the Disjoint Set (Union Find) algorithm.
"""
maze = [
    [0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0],
]

rows = np.shape(maze)[0]
columns = np.shape(maze)[1]

start = maze[0][0]
end = maze[rows-1][columns-1]

print(start, end)


number_of_cells = rows * columns

#   numcells = numrows * numcols;
#   Partition p(numcells); // p represents the maze components

#   // goal is not reachable from start
#   while (!p.Find(start, goal)) {
#     edge = randomly select a wall;
#     x = edge.x;
#     y = edge.y;
#     if(!p.Find(x,y)) {
#       remove edge;
#       // x and y now in same component
#       p.Union(x,y);
#     }
#   }
