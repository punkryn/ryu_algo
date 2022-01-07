# https://www.acmicpc.net/problem/15970

import sys
n = int(sys.stdin.readline())
coordinate = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
coordinate.sort(key=lambda x: (x[1], x[0]))
# print(coordinate)
prevColor = coordinate[0][1]
answer = 0
for i, co in enumerate(coordinate):
    pos, color = co
    if i == 0:
        answer += (coordinate[1][0] - coordinate[0][0])
    elif i == n - 1:
        answer += (coordinate[i][0] - coordinate[i-1][0])
    else:
        if coordinate[i][1] == coordinate[i-1][1] and coordinate[i][1] == coordinate[i+1][1]:
            answer += min(coordinate[i][0] - coordinate[i-1][0], coordinate[i+1][0] - coordinate[i][0])
        elif coordinate[i][1] == coordinate[i-1][1]:
            answer += (coordinate[i][0] - coordinate[i-1][0])
        elif coordinate[i][1] == coordinate[i+1][1]:
            answer += (coordinate[i + 1][0] - coordinate[i][0])

print(answer)