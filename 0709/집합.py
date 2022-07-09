# https://www.acmicpc.net/problem/11723
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    m = int(si())
    s = 1 << 21
    for _ in range(m):
        op = si().strip()
        if op == "all":
            s = (1 << 21) - 1
        elif op == 'empty':
            s = 0
        else:
            op, n = op.split()
            n = int(n)
            if op == 'add':
                s |= (1 << n)
            elif op == 'remove':
                s &= ~(1 << n)
            elif op == 'check':
                if s & (1 << n):
                    print(1)
                else:
                    print(0)
            elif op == 'toggle':
                s ^= (1 << n)