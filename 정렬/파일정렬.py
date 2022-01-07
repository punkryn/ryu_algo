# https://www.acmicpc.net/problem/20291

import sys
n = int(sys.stdin.readline())
files = [sys.stdin.readline().strip() for _ in range(n)]
ext_set = {}
for file in files:
    filename, ext = file.split('.')
    if ext not in ext_set:
        ext_set[ext] = 1
    else:
        ext_set[ext] += 1

for item in sorted(ext_set.items()):
    sys.stdout.write(item[0] + ' ' + str(item[1]) + '\n')