"""
UVA 10422 - Knights in FEN
Searching strategy: IDDS
"""

true, false = True, False


# region Method Descriptions


def scan(t=int):
    scanned = input().split()
    len_scan = len(scanned)
    if len_scan is 1:
        return t(scanned[0])

    for i in range(len_scan):
        scanned[i] = t(scanned[i])

    return scanned


def make_copy_of(original):
    copy = []
    for row in original:
        copy.append([val for val in row])

    return copy


def get_children(parent):
    i, j = 0, 0
    for i, row in enumerate(parent):
        for j, cell in enumerate(row):
            if cell is ' ':
                break
    children = set()
    if i > 0:
        if j > 1:
            child = make_copy_of(parent)
            horse = child[i - 1][j - 2]
            child[i][j] = horse
            child[i - 1][j - 2] = ' '
            children.add(child)
        if j < 3:
            child = make_copy_of(parent)
            horse = child[i - 1][j + 2]
            child[i][j] = horse
            child[i - 1][j + 2] = ' '
            children.add(child)
    if i > 1:
        if j > 0:
            child = make_copy_of(parent)
            horse = child[i - 2][j - 1]
            child[i][j] = horse
            child[i - 2][j - 1] = ' '
            children.add(child)
        if j > 1:


def is_target(graph):
    return graph is [
        ['1', '1', '1', '1', '1'],
        ['0', '1', '1', '1', '1'],
        ['0', '0', ' ', '1', '1'],
        ['0', '0', '0', '0', '1'],
        ['0', '0', '0', '0', '0']
    ]


def dls_recursive(graph, visited, depth, max_depth):
    if depth is max_depth:
        if is_target(graph):
            return true
        return false

    children = get_childre(graph)


def dls(graph, max_depth):
    if is_target(graph):
        return true
    visited = [graph]
    return dls_recursive(graph, visited, 0, max_depth)


# endregion


def main():
    N = scan()
    for n in range(N):
        graph = []
        for i in range(5):
            graph.append(list(input()))

        solved = false
        for i in range(10):
            if dls(graph, i):
                print("Solvable in {} move(s).".format(i + 1))
                solved = true
                break
        if not solved:
            print("Unsolvable in less than 11 move(s).")


main()
