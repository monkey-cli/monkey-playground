import numpy as np
from turtle import Screen, Turtle
import os
import sys
cwd = os.getcwd()

# ------------------------------------------------------------------------------------

def import_module_by_path(path):
    name = os.path.splitext(os.path.basename(path))[0]
    if sys.version_info[0] == 2:
        # Python 2
        import imp
        return imp.load_source(name, path)
    elif sys.version_info[:2] <= (3, 4):
        # Python 3, version <= 3.4
        from importlib.machinery import SourceFileLoader
        return SourceFileLoader(name, path).load_module()
    else:
        # Python 3, after 3.4
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod


# ------------------------------------------------------------------------------------
# Imports
mock = import_module_by_path(cwd + '/union_find_maze/mock.py')

visualizer_utils = import_module_by_path(
    cwd + '/union_find_maze/visualizer/utils.py')
draw_graph, fill_matrix = visualizer_utils.draw_graph, visualizer_utils.fill_matrix


# ------------------------------------------------------------------------------------

def init_screen():
    screen = Screen()
    screen.setup(1.0, 1.0)  # display size window
    turtle = Turtle(visible=False)  # hide the cursor completely
    turtle.speed(0)
    # screen sizes
    width, height = screen.window_width(), screen.window_height()


def wait_screen():
    screen = Screen()
    screen.tracer(True)
    screen.mainloop()

# ------------------------------------------------------------------------------------


def create_matrix(onComplete=None):
    init_screen()
    # matrix specs
    maze = mock.get_maze()
    matrix_rows, matrix_columns = np.shape(maze)[0],  np.shape(maze)[1]
    draw_graph(matrix_rows, matrix_columns)
    # fill walls and matrix edges
    fill_matrix(maze, matrix_rows, matrix_columns)

    if onComplete:
        onComplete()
    wait_screen()


def fill_coordinate(coordinate):
    print(coordinate)
