from visualizer.maze_visualizer import create_matrix, fill_coordinate
from maze import run_union_find


def on_next_step():
    print("next step")

def onRenderComplete():
    print("Maze render complete.\nProceeding to path finding")
    run_union_find()

create_matrix(onRenderComplete)


