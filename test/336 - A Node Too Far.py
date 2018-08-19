"""
UVA 336 - A Node Too Far
Searching strategy: IDS
"""

from queue import LifoQueue as Queue

true, false = True, False


# region Method Descriptions

def init_array(_n):
    return [[] for _i in range(_n)]


def scan(t=int):
    scanned = input().split()
    len_scan = len(scanned)
    if len_scan is 1:
        return t(scanned[0])

    for _i in range(len_scan):
        scanned[_i] = t(scanned[_i])

    return scanned


def ids(_root, _graph):
    _n = len(_graph)
    _levels = [-1] * _n
    _levels[_root] = 0
    q = Queue()
    q.put(_root)

    while not q.empty():
        front = q.get()
        for node in _graph[front]:
            if _levels[node] is -1:
                _levels[node] = _levels[front] + 1
                q.put(node)

    return _levels


def count_unreachables(_levels, ttl):
    _unreachables = 0
    for level in _levels:
        if level > ttl:
            _unreachables += 1

    return _unreachables

    # endregion


case_count = 1
n = scan()
while n:
    nodes = []
    graph = []
    c = 0
    while c < n:
        edges = scan()
        num_pairs = int(len(edges) / 2)
        c += num_pairs
        for i in range(num_pairs):
            x = edges[i * 2]
            y = edges[i * 2 + 1]

            if x not in nodes:
                nodes.append(x)
                graph.append([])
            if y not in nodes:
                nodes.append(y)
                graph.append([])

            u = nodes.index(x)
            v = nodes.index(y)
            graph[u].append(v)
            graph[v].append(u)

    job_done = false
    while not job_done:
        query = scan()
        num_queries = int(len(query) / 2)
        for i in range(num_queries):
            root = query[i * 2]
            distance = query[i * 2 + 1]
            if root is distance and distance is 0:
                job_done = true
                break

            levels = ids(nodes.index(root), graph)
            unreachables = count_unreachables(levels, distance)

            print("Case {}: {} nodes not reachable from node {} with TTL = {}.".format(
                case_count, unreachables, root, distance
            ))
            case_count += 1

    n = scan()
