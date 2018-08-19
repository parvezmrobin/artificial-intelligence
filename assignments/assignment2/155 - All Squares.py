"""
UVA 155 - All Squares
Searching strategy: IDS
"""

cx, cy, total = [0] * 3
true, false = True, False


def scan(t=int):
    scanned = input().split()
    len_scan = len(scanned)
    if len_scan is 1:
        return t(scanned[0])

    return [t(val) for val in scanned]


def depth_limited_search(x, y, k, level, max_level):
    if k is 0:
        return true
    if level is max_level:
        return false

    global cx, cy, total
    if (x - k <= cx <= x + k) and (y - k <= cy <= y + k):
        total += 1

    return (
            depth_limited_search(x + k, y + k, int(k / 2), level + 1, max_level) and
            depth_limited_search(x + k, y - k, int(k / 2), level + 1, max_level) and
            depth_limited_search(x - k, y + k, int(k / 2), level + 1, max_level) and
            depth_limited_search(x - k, y - k, int(k / 2), level + 1, max_level)
    )


def main():
    global cx, cy, total
    while true:
        k, cx, cy = scan()
        if k is cx is cy is 0:
            break

        depth_limit = 11  # log2(1024) = 10
        for max_depth in range(depth_limit):
            total = 0
            if depth_limited_search(1024, 1024, k, 0, max_depth):
                print('%3d' % total)
                break


main()
