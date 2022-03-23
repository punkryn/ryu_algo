# https://www.acmicpc.net/problem/10427
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(si())):
        _input = list(map(int, si().split()))
        n, a = _input[0], _input[1:]
        a.sort()
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + a[i - 1]
        
        ans = 0
        for i in range(2, n + 1):
            s = -1
            for j in range(1, n - i + 2):
                if s == -1:
                    s = a[j + i - 2] * i - (ps[j + i - 1] - ps[j - 1])
                else:
                    s = min(s, a[j + i - 2] * i - (ps[j + i - 1] - ps[j - 1]))
            ans += s
        print(ans)