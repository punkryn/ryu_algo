# https://www.acmicpc.net/problem/21315
import sys
import math
si = sys.stdin.readline

def go(cur, depth, k):
    if len(cur) == 1:
        return cur

    length = len(cur)
    ret = []
    sp = length - (2 ** (k - depth + 1))
    ret += go(cur[sp:], depth + 1, k) + cur[:sp]
    return ret

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))

    original = list(range(1, n + 1))
    for i in range(1, int(math.log2(n)) + 1):
        for j in range(1, int(math.log2(n)) + 1):
            if go(go(original, 1, i), 1, j) == a:
                print(i, j)
                exit()