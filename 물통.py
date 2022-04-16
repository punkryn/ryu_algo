# https://www.acmicpc.net/problem/2251
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    bowl = list(map(int, si().split()))
    a, b, c = bowl
    visited = set()

    q = deque()
    q.append([0, 0, c])
    visited.add((0, 0, c))
    ans = []
    while q:
        cur = q.popleft()

        for i in range(3):
            for j in range(3):
                if i == j: continue
                # i -> j·Î º×±â
                if cur[i] > bowl[j] - cur[j]:
                    cur[i] -= (bowl[j] - cur[j])
                    cur[j] = bowl[j]
                else:
                    cur[j] += cur[i]
                    cur[i] = 0
                
                if (cur[0], cur[1], cur[2]) not in visited:
                    visited.add((cur[0]))