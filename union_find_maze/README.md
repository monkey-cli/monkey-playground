# Maze solver using the union find algorithm

Maze representation:

|       |       |       |       |       |       |       |       |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **0** | **0** | 1     | 1     | 1     | 0     | 1     | 1     |
| 1     | **0** | 1     | 1     | 0     | 1     | 0     | 0     |
| 0     | **0** | **0** | 1     | 0     | 1     | 0     | 1     |
| 1     | 1     | **0** | **0** | 1     | 1     | 1     | 0     |
| 0     | 1     | 1     | **0** | **0** | **0** | **0** | 1     |
| 1     | 0     | 1     | 1     | 1     | 1     | **0** | **0** |

Start at (0,0), end at (5,7)/last coordinate

## Task:

Try to find the route in the provided maze from origin (0,0) to destination (N-1,M-1). N-number of rows, M-number of columns.

The maze is represented as a matrix of bits, where 0 represents an empty slot and 1 represents a wall.

```
    # 0 -> empty
    # 1 -> wall
```

Find the connected coordinates with value of 0 that connect from start to destination.

To solve the problem we will use the Disjoint Set (Union Find) algorithm.
The provided implementation of union-find includes path compression as well in its `find` operation.

## Edge cases

It is possible that the implementation can end up in "dead ends", coordinates that there is no next position to go to. In these cases the implementation will trance back the steps to find the first node that has a possible next step to go to that is not part of the connected dataset (not part of the current route).

## Visualized example

To run visualizer of the union-find maze solver run `./union_find_maze/main.py`. The graphical tool will update until the start and the end of the maze are connected.

```
# Graphical units

1. green - represents the start and the end of the maze
2. yellow - represents the traversed route from start to end.
3. red - in case of a dead-end. The coordinate will be marked with red.
```
| 10x10 maze | 20x20 maze |
|-|-|
|<img src="https://github.com/monkey-cli/monkey-playground/blob/master/assets/union_find_maze/10x10%20maze.gif" width="500" height="auto"/>| <img src="https://github.com/monkey-cli/monkey-playground/blob/master/assets/union_find_maze/20x20%20maze.png" width="500"  height="auto"/>|

The maze creation is responsive to the matrix size and will scale to fil the screen of the running device and the sizes of the matrix boxes will adapt their height according to the screen size and the actual size of the matrix/maze being rendered.

To customize and/or create new mazes, check out `./union_find_maze/mock.py`.
