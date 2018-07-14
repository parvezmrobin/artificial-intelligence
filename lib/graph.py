from math import inf
from utils import printf

true, false = True, False


class Graph:
    def __init__(self, n, edges=None, bidirectional=True):
        self.graph = [[] for i in range(n)]

        if edges is not None:
            for frm, to in edges:
                self.add_edge(frm, to, bidirectional)

    def add_edge(self, frm, to, bidirectional=True):
        self.graph[frm].append(to)
        if bidirectional:
            self.graph[to].append(frm)

    def levels(self, root=0):
        n = len(self.graph)
        level = [-1] * n
        level[root] = 0

        stack = [root]
        while stack:
            frm = stack.pop()
            for to in self.graph[frm]:
                if level[to] is -1:
                    level[to] = level[frm] + 1
                    stack.append(to)

        return level

    def dfs(self, root, target, max_depth=inf, print_path=true, print_backtrack=true):
        if root is target:
            return true

        n = len(self.graph)
        levels = [-1] * n
        levels[root] = 0
        printf("Searching Sequence:", root, ' ')

        return self.dfs_recursive(root, target, levels, max_depth, false, print_path, print_backtrack)

    def dfs_recursive(self, root, target, levels, max_depth=inf, iterative_deepening=false, print_path=true,
                      print_backtrack=true):
        if not iterative_deepening and Graph.match(root, target):
            return true

        if levels[root] is max_depth:
            if Graph.match(root, target):
                return true
            return false

        for child in self.graph[root]:
            if levels[child] is -1:
                levels[child] = levels[root] + 1

                if print_path:
                    printf(child, ' ')

                if self.dfs_recursive(child, target, levels, max_depth, iterative_deepening, print_path,
                                      print_backtrack):
                    return true

                if print_backtrack:
                    printf(root, ' ')
        return false

    def dls(self, root, target, max_depth, print_path=true, print_backtrack=true):
        return self.dfs(root, target, max_depth, print_path, print_backtrack)

    def ids(self, root, target, max_depth=inf, print_path=true, print_backtrack=true):
        if max_depth is inf:
            depth = 0
            while true:
                if self.dls(root, target, depth, print_path, print_backtrack):
                    return depth
                print('')
                depth += 1

        for depth in range(max_depth):
            if self.dls(root, target, depth, print_path, print_backtrack):
                return depth
        return None

    @staticmethod
    def match(root, target):
        return root is target
