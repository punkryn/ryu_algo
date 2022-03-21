# https://www.acmicpc.net/problem/14889
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    s = [list(map(int, si().split())) for _ in range(n)]

    ans = int(1e9)
    x = [0] * n
    
    for i in range(n):
        for j in range(n):
            x[i] += s[i][j]
            x[j] += s[i][j]
    
    half = 0
    for i in range(n):
        half += x[i]
    half //= 2

    save = x[0]
    def go(depth, v):
        nonlocal ans, save, half
        if depth == 0:
            ans = min(ans, abs(save - half))
            return
        
        for i in range(v + 1, n - depth + 1):
            save += x[i]
            go(depth - 1, i)
            save -= x[i]
    go(n // 2 - 1, 0)

    print(ans)

if __name__ == '__main__':
    main()
