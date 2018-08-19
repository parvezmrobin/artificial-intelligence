"""
UVA 112 - Tree Summing
Searching strategy: DFS
"""

true, false = True, False
space, parenthesis_start, parenthesis_close = ' ', '(', ')'
graph = {}
input_line = ''
i = 0


def read_char():
    global i, input_line
    while i is not len(input_line):
        input_line = input()
        i = 0
    char = input_line[i]
    i += 1
    while char.isspace():
        char = input_line[i]
        i += 1

    return char


def build_tree_recursive():
    char = read_char()
    if char is parenthesis_close:
        return []
    root = ''
    while char is not parenthesis_start:
        root += char
        char = read_char()

    root = int(root)
    graph[root] = build_tree_recursive()


def build_tree_from_console():
    char = read_char()
    target_sum = ''
    while char is not ' ':
        target_sum += char
        char = read_char()
    target_sum = int(target_sum)

    return build_tree_recursive(), target_sum


def main():
    root, target_sum = build_tree_from_console()


main()
