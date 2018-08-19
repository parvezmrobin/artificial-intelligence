"""
UVA 441 - Lotto
Searching strategy: DFS
Unsolved
"""

true, false = True, False
A, ans, n = [], [0] * 6, 0


# region Method Descriptions


def scan(t=int):
    scanned = input().split()
    len_scan = len(scanned)

    for i in range(len_scan):
        scanned[i] = t(scanned[i])

    return scanned


def dfs(idx, i):
    if idx == 6:
        print(ans[0], end='')
        i = 1
        while i < 6:
            print('', ans[i], end='')
            i += 1
        print('')
        return

    while i < n:
        ans[idx] = A[i]
        dfs(idx + 1, i + 1)
        i += 1


# endregion


first = 1
while true:
    line = scan()
    n = line[0]
    if n is 0:
        break
    if first is not 1:
        print('')
    first = 0
    A = line[1:]
    dfs(0, 0)

