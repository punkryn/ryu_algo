# 4 6
# a t c i s w

import sys

L, C = map(int, sys.stdin.readline().split())
arr = sorted(sys.stdin.readline().split())

used = [0] * C
def go(depth, cur, start):
    if depth == L:
        m_cnt = 0
        j_cnt = 0
        for w in cur:
            if w in 'aeiou':
                m_cnt += 1
            else:
                j_cnt += 1
        
        if m_cnt >= 1 and j_cnt >= 2:
            sys.stdout.write(''.join(cur) + '\n')
        return

    for i in range(start, C):
        if used[i] == 0:
            used[i] = 1
            cur.append(arr[i])
            go(depth + 1, cur, i + 1)
            cur.pop()
            used[i] = 0

go(0, [], 0)