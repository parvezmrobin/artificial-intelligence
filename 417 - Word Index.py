"""
UVA 417 - Word Index
Searching strategy: DFS
"""

from queue import Queue

M = {}
true, false = True, False


def inc_char(value):
    return chr(ord(value) + 1)


def generate_positions():
    q = Queue()
    c = 'a'
    while c <= 'z':
        q.put(c)
        c = inc_char(c)

    cnt = 1

    while not q.empty():
        s = q.get()
        M[s] = cnt
        cnt += 1

        if len(s) is 5:
            continue

        c = inc_char(s[len(s) - 1])
        while c <= 'z':
            q.put(s + c)
            c = inc_char(c)


generate_positions()

more_entry = true
while more_entry:
    try:
        s = input()
        if s in M:
            print(M[s])
        else:
            print(0)
    except EOFError:
        more_entry = false
