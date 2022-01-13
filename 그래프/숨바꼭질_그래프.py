# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
si = sys.stdin.readline

def bfs(n, k):
    q = deque()
    q.append(n)
    visited = [-1] * (100001)
    visited[n] = 0
    def move(y, d):
        if y < 0 or y > 100000 or visited[y] != -1:
            return
        visited[y] = d
        q.append(y)
    
    while q:
        x = q.popleft()
        move(x - 1, visited[x] + 1)
        move(x + 1, visited[x] + 1)
        move(x * 2, visited[x] + 1)
    return visited

def main():
    global ans
    n, k = map(int, si().split())
    if n < k:
        ans = bfs(n, k)
        print(ans[k])
    else:
        print(n - k)

if __name__ == '__main__':
    main()