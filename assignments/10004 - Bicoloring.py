"""
UVA 10004 - Bicoloring
Searching strategy: DFS
"""

true, false = True, False


# region Method Definitions
def init_array(n1, n2=None, value=false):
    if n2 is None:
        n2 = n1
    return [[value] * n2 for i in range(n1)]


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
    n = scan()
    if n is 0:
        break

    a = init_array(n)
    color = [-1] * n
    color[0] = 0

    num_edge = scan()
    for i in range(num_edge):
        x, y = scan()
        a[x][y] = true
        a[y][x] = true

    stack = [0]
    colorable = true
    while colorable and stack:
        i = stack.pop()
        for j in range(n):
            if a[i][j]:
                if color[j] is -1:
                    color[j] = color[i] ^ 1
                    stack.append(j)
                elif color[j] == color[i]:
                    colorable = false
                    break

    if colorable:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
