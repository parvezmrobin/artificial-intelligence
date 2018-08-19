"""
UVA 280 - Vertex
Searching strategy: BFS
"""

from queue import LifoQueue

true, false = True, False


# region Method Descriptions

def init_array(n):
    return [set() for i in range(n)]


def scan(t=int):
    scanned = input().split()
    len_scan = len(scanned)
    if len_scan is 1:
        return t(scanned[0])

    for i in range(len_scan):
        scanned[i] = t(scanned[i])

    return scanned


def bfs(graph, root):
    n = len(graph)
    visited = [false] * n
    stack = LifoQueue()
    stack.put(root)

    while not stack.empty():
        frm = stack.get()

        for to in graph[frm]:
            if not visited[to]:
                visited[to] = true
                stack.put(to)

    return list(filter(lambda x: not visited[x], list(range(n))))


# endregion


def main():
    n = scan()
    while n:
        graph = init_array(n)
        while true:
            edges = scan()
            if edges is 0:
                break
            frm = edges[0]
            for to in edges[1: -1]:
                graph[frm - 1].add(to - 1)
                frm = to

        queries = scan()[1:]

        for query in queries:
            unvisited = bfs(graph, query-1)
            print(len(unvisited), '', end='')
            for node in unvisited:
                print(node + 1, '', end='')
            print('')

        n = scan()


main()
