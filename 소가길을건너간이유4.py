import sys
from heapq import heappush, heappop
si = sys.stdin.readline

if __name__ == '__main__':
    c, n = map(int, si().split())
    t = sorted([int(si()) for _ in range(c)])
    ab = []
    for _ in range(n):
        a, b = map(int, si().split())
        heappush(ab, (b, a))
    check = [False] * c

    ans = 0
    while ab:
        e, s = heappop(ab)
        for i in range(c):
            if t[i] >= s and t[i] <= e and not check[i]:
                ans += 1
                check[i] = True
                break
        
    print(ans)