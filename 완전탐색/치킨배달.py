# https://www.acmicpc.net/problem/15686
import sys
si = sys.stdin.readline
INF = int(1e9)

def go(depth, cur, prev):
    global ans
    if depth == 0:
        total = 0
        for house in houses:
            tmp = INF
            for c in cur:
                tmp = min(tmp, abs(chickens[c][0] - house[0]) + abs(chickens[c][1] - house[1]))
            total += tmp
        ans = min(ans, total)
        return
    
    for i in range(prev + 1, len(chickens) - depth + 1):
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
    
    ans = INF
    go(m, [], -1)
    print(ans)