# https://www.acmicpc.net/problem/10825

import sys

n = int(sys.stdin.readline())

infos = []
for _ in range(n):
    name, a, b, c = sys.stdin.readline().split()
    infos.append([name, int(a), int(b), int(c)])

infos.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for info in infos:
    sys.stdout.write(info[0] + '\n')