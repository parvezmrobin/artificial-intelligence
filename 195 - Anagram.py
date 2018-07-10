"""
UVA 195 - Anagram
Searching strategy: DFS
"""

from queue import Queue

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


# endregion

T = scan()
for t in range(T):
    base_word = input()
    gen = {base_word: None}
    str_len = len(base_word)

    prev_swap = None
    q = Queue()
    q.put(tuple(base_word))

    while not q.empty():
        word = q.get()
        for i in range(str_len - 1):
            if i is not gen[''.join(word)] and word[i] is not word[i + 1]:
                new_word = list(word)
                new_word[i] = word[i + 1]
                new_word[i + 1] = word[i]

                new_word = ''.join(new_word)
                if new_word not in gen.keys():
                    q.put(tuple(new_word))
                    gen[''.join(new_word)] = i

    words = sorted(sorted(gen.keys()), key=str.upper)
    for word in words:
        print(word)
