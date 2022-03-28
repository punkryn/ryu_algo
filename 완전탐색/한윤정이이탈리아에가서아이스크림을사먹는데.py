# https://www.acmicpc.net/problem/2422
si = __import__('sys').stdin.readline

def go(depth, cur, prev):
    global ans
    if depth == 0:
        for i in range(2):
            for j in range(i + 1, 3):
                if comb[cur[i]][cur[j]] or comb[cur[j]][cur[i]]:
                    return
        else:
            ans += 1
        return
    
    for i in range(prev + 1, n - depth + 2):
        cur.append(i)
        go(depth - 1, cur, i)
        cur.pop()

if __name__ == '__main__':
    n, m = map(int, si().split())
    comb = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, si().split())
        comb[x][y] = 1
        comb[y][x] = 1
    
    ans = 0
    go(3, [], 0)
    print(ans)