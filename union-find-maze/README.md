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
