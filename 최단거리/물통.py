# https://www.acmicpc.net/problem/2251
import sys
from collections import deque
import copy
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
        if cur[0] == 0:
            ans.append(cur[2])

        for i in range(3):
            for j in range(3):
                if i == j or cur[i] == 0: continue
                v = copy.deepcopy(cur)
                if cur[i] > bowl[j] - cur[j]:
                    v[i] -= (bowl[j] - cur[j])
                    v[j] = bowl[j]
                else:
                    v[j] += cur[i]
                    v[i] = 0
                
                if (v[0], v[1], v[2]) not in visited:
                    visited.add((v[0], v[1], v[2]))
                    q.append([v[0], v[1], v[2]])
    print(*sorted(ans))