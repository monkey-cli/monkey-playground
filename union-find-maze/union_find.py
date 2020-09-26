
# union find equipped with "path compression"
def find(data, i):
    root = i
    # Find the root of the dataset
    while (root != data[root]):
        root = data[root]

    # Compress the path leading back to the root.
    # this operation is called "path compression"
    while (i != root):
        next = data[i]
        data[i] = root
        i = next

    return root


def union(data, i, j):
    if (connected(data, i, j)):
        return
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj


def connected(data, i, j):
    return find(data, i) == find(data, j)


# ------------------------------------------------------------
# Test data
# ------------------------------------------------------------
# n = 10
# data = [i for i in range(n)]

# # connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
# connections = [(6, 1), (5, 6)]
# # union
# for i, j in connections:
#     union(data, i, j)

# # find
# for i in range(n):
#     print('item', i, '-> component', find_immediate(data, i))
