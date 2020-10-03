import numpy as np
from turtle import Screen, Turtle
from visualizer import utils
import mock


draw_graph, fill_matrix, fill_coordinate, is_matrix_edge = (
    utils.draw_graph,
    utils.fill_matrix,
    utils.fill_coordinate,
    utils.is_matrix_edge,
)

# ------------------------------------------------------------------------------------


def init_screen():
    screen = Screen()
    screen.setup(1.0, 1.0)  # display size window
    turtle = Turtle(visible=False)  # hide the cursor completely
    turtle.speed(0)
    # screen sizes
    # width, height = screen.window_width(), screen.window_height()


def wait_screen():
    screen = Screen()
    screen.tracer(True)
    screen.mainloop()


# ------------------------------------------------------------------------------------


def create_matrix(onComplete=None):
    init_screen()
    # matrix specs
    maze = mock.get_maze()
    matrix_rows, matrix_columns = np.shape(maze)[0], np.shape(maze)[1]
    draw_graph(matrix_rows, matrix_columns)
    # fill walls and matrix edges
    fill_matrix(maze, matrix_rows, matrix_columns)

    if onComplete:
        onComplete()
    wait_screen()


def on_step_reached(data):
    coordinate = data["value"]
    status = data["status"]

    maze = mock.get_maze()
    matrix_rows, matrix_columns = np.shape(maze)[0], np.shape(maze)[1]
    if not is_matrix_edge(maze, coordinate):
        fill_coordinate(
            coordinate,
            matrix_rows,
            matrix_columns,
            ("yellow" if status == "NEXT_STEP" else "red"),
        )
