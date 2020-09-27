import numpy as np
from turtle import Screen, Turtle
from utils import draw_graph, fill_coordinate, is_matrix_edge

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


# maze = [
#     [1, 1],
#     [1, 0],
# ]


screen = Screen()
screen.setup(1.0, 1.0)  # display size window
turtle = Turtle(visible=False)  # hide the cursor completely
turtle.speed(0)

# screen sizes
width, height = screen.window_width(), screen.window_height()
# matrix specs
matrix_rows, matrix_columns = np.shape(maze)[0],  np.shape(maze)[1]
# draw one more line than the actual matrix size
columns, rows = matrix_columns + 1, matrix_rows + 1

draw_graph(matrix_rows, matrix_columns)


for row in range(0, matrix_rows):
    for column in range(0, matrix_columns):
        if (is_matrix_edge(maze, (row, column))):
            fill_coordinate((row, column), matrix_rows,
                            matrix_columns, 'red')
        if(maze[row][column] == 1):  # fill a wall
            fill_coordinate((row, column), matrix_rows,
                            matrix_columns, 'black')

screen.tracer(True)
screen.mainloop()
