# https://www.acmicpc.net/problem/1713
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    n = int(si())
    total = int(si())
    number = list(map(int, si().split()))

    t = dict()
    for idx, num in enumerate(number):
        if num in t:
            t[num][0] += 1
        else:
            if len(t) == n:
                minv = min(t.items(), key=lambda x: (x[1][0], x[1][1]))[0]
                del t[minv]
            t[num] = [1, idx]
    print(*sorted(t.keys()))