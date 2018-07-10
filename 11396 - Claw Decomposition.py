"""
UVA 11396 - Claw Decomposition
Searching strategy: BFS
Unsolved
"""

from queue import Queue

true, false = True, False
black, white = 1, 0


# region Method Descriptions

def init_array(n):
    return [[] for i in range(n)]


def scan(t=int):
    scanned = input().split()
    len_scan = len(scanned)
    if len_scan is 1:
        return t(scanned[0])

    for i in range(len_scan):
        scanned[i] = t(scanned[i])

    return scanned


# endregion

while true:
    V = scan()
    if V is 0:
        break

    graph = init_array(V + 1)
    while true:
        u, v = scan()
        if u is v and v is 0:
            break
        graph[u].append(v)
        graph[v].append(u)

    q = Queue()
    q.put(1)
    colors = [-1] * (V + 1)
    colors[1] = 1

    yes = true
    while not q.empty() and yes:
        u = q.get()
        for v in graph[u]:
            if colors[v] is -1:
                colors[v] = 1 - colors[u]
                q.put(v)
            elif colors[v] is colors[u]:
                yes = false
                break

    print("YES" if yes else "NO")
