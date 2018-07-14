true, false = True, False


def scan(t=int, unpack=true):
    scanned = input().split()
    len_scan = len(scanned)
    if unpack and len_scan is 1:
        return t(scanned[0])

    for i in range(len_scan):
        scanned[i] = t(scanned[i])

    return scanned


def init_array(dim1, dim2=None, value=0):
    if dim2 is None:
        dim2 = dim1
    return [[value] * dim2 for dim in range(dim1)]


def printf(*args):
    print(*args, end='')
