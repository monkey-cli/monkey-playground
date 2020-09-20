import math
import numpy as np

# 0 -> empty
# 1 -> wall
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
