from turtle import Screen, Turtle
import numpy as np

turtle = Turtle(visible=False)  # hide the cursor completely
turtle.speed(0)


def draw_graph(num_rows, num_columns, space_from_edge=10):
    columns = num_columns + 1
    rows = num_rows + 1
    screen = Screen()
    width, height = screen.window_width(), screen.window_height()

    x = - (width/2 - space_from_edge)
    distanceX = width/columns
    for _ in range(columns):
        turtle.penup()
        turtle.goto(x, (height/2))
        turtle.pendown()
        turtle.goto((x, -(height/2)))
        x += distanceX

    y = (height/2 - space_from_edge)
    distanceY = height/rows
    for _ in range(rows):
        turtle.penup()
        turtle.goto((width/2), y)
        turtle.pendown()
        turtle.goto((-(width/2)), y)
        y -= distanceY


def fill_matrix(maze, matrix_rows, matrix_columns):
    for row in range(0, matrix_rows):
        for column in range(0, matrix_columns):
            if (is_matrix_edge(maze, (row, column))):
                fill_coordinate((row, column), matrix_rows,
                                matrix_columns, 'red')
            if(maze[row][column] == 1):  # fill a wall
                fill_coordinate((row, column), matrix_rows,
                                matrix_columns, 'black')


def fill_coordinate(coordinate, num_rows, num_columns, fill_color='red', space_from_edge=10):
    turtle.color(fill_color)
    turtle.fillcolor(fill_color)

    rows = num_rows + 1
    columns = num_columns + 1
    screen = Screen()
    width, height = screen.window_width(), screen.window_height()
    distanceX = width/columns
    distanceY = height/rows
    # x -> represents columns
    # y -> represents rows
    Y, X = coordinate[0], coordinate[1]

    # this is tested in MAC environment and the coordinate calculation is based on the mac-os display grid
    startX = -width/2 + X * distanceX + space_from_edge
    startY = height/2 - Y * distanceY - space_from_edge

    turtle.begin_fill()
    turtle.up()
    turtle.goto(startX, startY)
    turtle.down()
    # draw top
    turtle.forward(distanceX)
    # draw right
    turtle.right(90)
    turtle.forward(distanceY)
    # draw bottom
    turtle.right(90)
    turtle.forward(distanceX)
    # draw left
    turtle.right(90)
    turtle.forward(distanceY)
    turtle.right(90)
    turtle.end_fill()

    # reset colors back to default
    turtle.color("black")
    turtle.fillcolor("white")
    return []


def is_matrix_edge(matrix, coordinate):
    rows, columns = np.shape(matrix)[0],  np.shape(matrix)[1]
    X, Y = coordinate[0], coordinate[1]
    if(X == 0 and Y == 0):
        return True
    if(X == rows-1 and Y == columns - 1):
        return True
    return False
