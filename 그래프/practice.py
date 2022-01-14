import sys
from collections import deque

si = sys.stdin.readline

def move(pos, time, visited, q):
    if pos < 0 or pos > 100000:
        return
    if visited[pos] != -1:
        return
    
    visited[pos] = time
    q.append(pos)

def bfs(n, k, visited):
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        cur = q.popleft()

        if visited[k] != -1:
            break

        move(cur - 1, visited[cur] + 1, visited, q)
        move(cur + 1, visited[cur] + 1, visited, q)
        move(cur * 2, visited[cur] + 1, visited, q)

def main():
    n, k = map(int, si().split())
    visited = [-1] * 100001
    bfs(n, k, visited)
    print(visited[k])

if __name__ == '__main__':
    main()