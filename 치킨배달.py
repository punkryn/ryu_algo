# https://www.acmicpc.net/problem/15686
import sys
si = sys.stdin.readline
INF = int(1e9)

def go(depth, cur, prev):
    global ans
    if depth == 0:
        print(cur)
        total = 0
        for c in cur:
            total += distance[c]
        ans = min(ans, total)
        return
    
    for i in range(prev + 1, len(distance) - depth + 1):
        cur.append(i)
        go(depth - 1, cur, i)
        cur.pop()

if __name__ == '__main__':
    n, m = map(int, si().split())
    city = [list(map(int, si().split())) for _ in range(n)]
    chickens = []
    houses = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    
    distance = [INF] * len(chickens)
    for i in range(len(chickens)):
        for house in houses:
            distance[i] = min(distance[i], abs(house[0] - chickens[i][0]) + abs(house[1] - chickens[i][1]))
    
    ans = INF
    go(m, [], -1)
    print(ans)