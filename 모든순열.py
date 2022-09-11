# https://www.acmicpc.net/problem/10974
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(depth, cur=[]):
    if depth == n:
        print(*cur)
        return
    
    for i in range(n):
        if visited[i]: continue
        cur.append(i + 1)
        visited[i] = 1
        go(depth + 1, cur)
        visited[i] = 0
        cur.pop()

if __name__ == '__main__':
    n = int(si())
    visited = [0] * n
    go(0)