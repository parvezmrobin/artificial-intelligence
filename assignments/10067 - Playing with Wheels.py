"""
UVA 11396 - 10067 - Playing with Wheels
Searching strategy: IDDS
"""

from math import inf

true, false = True, False


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


def get_children(parent):
    return [
        ((parent[0] - 1) % 10, parent[1], parent[2], parent[3]),
        ((parent[0] + 1) % 10, parent[1], parent[2], parent[3]),
        (parent[0], (parent[1] - 1) % 10, parent[2], parent[3]),
        (parent[0], (parent[1] + 1) % 10, parent[2], parent[3]),
        (parent[0], parent[1], (parent[2] - 1) % 10, parent[3]),
        (parent[0], parent[1], (parent[2] + 1) % 10, parent[3]),
        (parent[0], parent[1], parent[2], (parent[3] - 1) % 10),
        (parent[0], parent[1], parent[2], (parent[3] + 1) % 10),
    ]


def dls_recursive(root, target, forbidden, visited, depth, max_depth):
    if depth is max_depth:
        if root is target:
            return depth
        return None
    # 6 5 0 8
    for child in get_children(root):
        if child not in forbidden and child not in visited:
            visited.add(child)
            if dls_recursive(child, target, forbidden, visited, depth + 1, max_depth):
                return true


def dls(root, target, forbidden, max_depth):
    visited = set()
    visited.add(root)
    return dls_recursive(root, target, forbidden, visited, 0, max_depth)


# endregion

def main():
    T = scan()
    for t in range(T):
        initial = tuple(scan())
        target = tuple(scan())
        N = scan()
        forbidden = []
        for n in range(N):
            forbidden.append(tuple(scan()))
        _ = scan()

        depth_limit = 10 ** 4
        max_depth = 0
        res = None
        while max_depth < depth_limit:
            res = dls(initial, target, forbidden, max_depth)
            if res is not None:
                print(res)
                break
            max_depth += 1

        if res is None:
            print(-1)


main()
