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
#     [0, 1],
#     [0, 0]
# ]


# Generate maze example from
# https://github.com/keesiemeijer/maze-generator
# Remove first and last rows as they represend the top and bottom borders
# For each row also ignore the first and last items since they represent the horizontal borders
maze20x20 = [
    "10000000001000001000000010000000000010001",
    "11111011101110111010111010111111101010101",
    "10001000100000100010001010100010001010101",
    "10101110111110101111101110101110111011101",
    "10100000101000100000100010101000101010001",
    "10111111101011111110111010101011101010101",
    "10001010000010000010101000101000101000101",
    "11101010111111111010101111101110101111101",
    "10001000000010000010001000001000100010001",
    "10111111111010111011101110111011111010111",
    "10000010001000100010100010001000100010101",
    "10111011101011101110111010101110101010101",
    "10101000100000101000001010101000101010101",
    "10101110101110101011111011101011101110101",
    "10000010100010001010000010001010001000101",
    "11111010111011111010111110111010111011101",
    "10001010101010001010100010100010100010001",
    "11101010101010101010101010101110101110101",
    "10001010100010100010001000101000001000101",
    "10111010111010101111111110101011111111101",
    "10100010001000101000000000101000000000101",
    "10101111101011111011111111101110111110101",
    "10000010001010000010000000001010100010001",
    "11111110111110111110111111111010101011101",
    "10000000100000100010100000000010101000101",
    "10111110101111111010111111111010101110101",
    "10000010101000000010001000001000100010101",
    "11111010101110101011101011101111101110101",
    "10001010100010101010001000100000101000101",
    "10101011111010101110111110111110101011101",
    "10100010000010100010000000000010101000101",
    "10111110111111111011111111111110101110111",
    "10000000100010000000001000100000100010001",
    "10111111101010111111101010101110111011111",
    "10100000001010000010100010100010001010001",
    "10111111101011111010111110111011111010101",
    "10000000001010001010100000101000000010101",
    "11111111111010101010101111101111111110101",
    "10000000000000100010000000000000000000101",
]

maze5x4 = [
    "10001000101",
    "10101010101",
    "10100010101",
    "10111110101",
    "10001010101",
    "10101010101",
    "10101000001",
]

maze10x10 = [
    "100000000000100000001",
    "101010111111101111101",
    "101010100000001000001",
    "111010101111111011101",
    "100010100000101010101",
    "101111111110101010101",
    "101000000010101010101",
    "101011101110101010101",
    "100010101000101010001",
    "101110101011101010111",
    "101000101010001010001",
    "101110101010101011101",
    "100010100000101000101",
    "111010111111111110111",
    "100010000010000010001",
    "101111101010111011101",
    "101000001010101010001",
    "101011111011101010101",
    "100010000000001000101",
]


def construct_maze(maze_template):
    temp_maze = []
    for row in maze_template:
        valid_row = row[1 : len(row) - 1]  # remove 1st and last item
        split_row = [int(x) for x in valid_row]
        temp_maze.append(split_row)
    return temp_maze


# ---------------------------------------------------------------
maze = construct_maze(maze10x10)


def get_maze():
    return maze
