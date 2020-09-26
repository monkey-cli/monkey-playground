
"""
Disjoint Set Union (Union Find)
https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
"""


def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]


def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj


def connected(data, i, j):
    return find(data, i) == find(data, j)
