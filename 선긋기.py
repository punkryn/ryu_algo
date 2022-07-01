# https://www.acmicpc.net/problem/2170
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    pos = sorted([list(map(int, si().split())) for _ in range(n)])
    ans = 0
    px, py = pos[0][0], pos[0][1]
    for x, y in pos[1:]:
        if x <= py:
            py = max(py, y)
        else:
            ans += py - px
            px = x
            py = y
    ans += py - px
    print(ans)