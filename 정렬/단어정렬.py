# https://www.acmicpc.net/problem/1181

import sys
n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]
words.sort(key=lambda x: (len(x), x))

prev = ''
for word in words:
    if word == prev:
        continue

    sys.stdout.write(word + '\n')
    prev = word