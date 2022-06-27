# https://www.acmicpc.net/problem/1484
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    g = int(si())
    ans = []
    for i in range(1, g + 1):
        if i * i > g:
            break

        if g % i != 0:
            continue

        b = i
        a = g // i
        if a == b:
            continue

        if (a + b) % 2 == 0:
            ans.append((a + b) // 2)
    
    if ans:
        for a in sorted(ans):
            print(a)
    else:
        print(-1)