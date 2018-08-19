"""
UVA 193 - Graph Coloring
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


def main():
    T = scan()
    for t in range(T):
        n, k = scan()

        graph = init_array(n + 1)

        for i in range(k):
            x, y = scan()
            graph[x].append(y)
            graph[y].append(x)

        q = Queue()
        q.put(1)
        color = [-1] * (n + 1)
        color[1] = black
        count_black = 1

        while not q.empty():
            i = q.get()
            for j in graph[i]:
                if color[j] is -1:
                    color[j] = color[i] ^ 1
                    q.put(j)

                    if color[j]:
                        count_black += 1

        if count_black > n - count_black:
            count_black = filter(
                lambda x: x,
                map(lambda i, c: i if c else None, enumerate(color))
            )
        else:
            count_black = n - count_black
            colored_black = filter(
                lambda x: x,
                map(lambda i, c: None if c else i, enumerate(color))
            )

        print(len(count_black))
        print(count_black)


main()
