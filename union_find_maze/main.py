from visualizer.maze_visualizer import create_matrix, on_step_reached
from maze import run_union_find


def on_step_update(data):
    """
    Callback method to be called on every next step update from the union find runtime.
    Example: 
    1. new step was found
    2. dead-end reached
    """
    on_step_reached(data)


def onRenderComplete():
    print("Maze render complete.\nProceeding to path finding...")
    run_union_find(on_step_update)

# trigger and matrix render and after that is done start solving the maze
create_matrix(onRenderComplete)
