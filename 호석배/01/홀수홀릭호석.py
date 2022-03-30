# https://www.acmicpc.net/problem/20164
import sys
si = sys.stdin.readline

def go(n, ans):
    global minv, maxv
    if len(n) == 1:
        ans = ans + (1 if int(n) % 2 == 1 else 0)
        minv = min(ans, minv)
        maxv = max(ans, maxv)
        return
    
    elif len(n) == 2:
        total = 0
        total = total + (1 if int(n[0]) % 2 == 1 else 0) + (1 if int(n[1]) % 2 == 1 else 0)
        nxt = str(int(n[0]) + int(n[1]))
        go(nxt, ans + total)
    
    elif len(n) >= 3:
        total = 0
        for i in range(len(n)):
            if int(n[i]) % 2 == 1:
                total += 1

        for i in range(1, len(n) - 1):
            for j in range(i + 1, len(n)):
                nxt = str(int(n[:i]) + int(n[i:j]) + int(n[j:]))
                go(nxt, ans + total)

if __name__ == '__main__':
    n = si().strip()
    minv = 1e9
    maxv = 0
    go(n, 0)
    print(minv, maxv)