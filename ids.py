"""
Iterative Deepening Search
"""

from queue import LifoQueue

true, false = True, False

n = 11
graph = [[] for i in range(n)]


def add_edge(_frm, _to):
    graph[_frm].append(_to)
    graph[_to].append(_frm)


edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6),
    (3, 7),
    (3, 8),
    (4, 9),
    (4, 10)
]

for frm, to in edges:
    add_edge(frm, to)


def match_value(val1, val2):
    return val1 is val2


def dfs(graph, root, value, depth_limit):
    path = []
    q = LifoQueue()
    q.put(root)
    level = [-1] * len(graph)
    level[root] = 0
    print("Searching sequence:", end=' ')
    while not q.empty():
        frm = q.get()
        print(frm, end=' ')

        if depth_limit == level[frm]:
            if match_value(frm, value):
                return true
            continue

        for to in graph[frm]:
            if level[to] is -1:
                level[to] = level[frm] + 1
                q.put(to)

    return false


max_depth = 20
for i in range(4, max_depth):
    if dfs(graph, 4, 5, i):
        print('')
        print("Found in depth {}".format(i))
        break
    print('')
