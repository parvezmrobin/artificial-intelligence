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


def dfs(graph, root, value):
    q = LifoQueue()
    q.put(root)
    level = [-1] * len(graph)
    print("Searching sequence:", end=' ')
    while not q.empty():
        frm = q.get()
        print(frm, end=' ')
        if frm is value:
            return true

        if not level[frm]:
            level[frm] = true
            for to in graph[frm]:
                q.put(to)

    return false


dfs(graph, 1, 7)
