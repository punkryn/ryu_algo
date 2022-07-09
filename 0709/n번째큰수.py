# https://www.acmicpc.net/problem/2075
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    table = [list(map(int, si().split())) for _ in range(n)]
    cand = []
    for i in range(n):
        heapq.heappush(cand, (-table[-1][i], i))
    h = [n - 1] * n
    ans = 0
    for i in range(n):
        mv, idx = heapq.heappop(cand)
        h[idx] -= 1
        heapq.heappush(cand, (-table[h[idx]][idx], idx))
        ans = -mv
    print(ans)