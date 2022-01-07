# https://www.acmicpc.net/problem/11652

import sys
n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]

dic = {}
for card in cards:
    if card not in dic:
        dic[card] = 1
    else:
        dic[card] += 1

maxvalue = max(dic.values())
minvalue = 2 ** 64
for key in dic:
    if dic[key] == maxvalue:
        if key < minvalue:
            minvalue = key

print(minvalue)