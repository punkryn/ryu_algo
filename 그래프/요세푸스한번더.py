# https://www.acmicpc.net/problem/6523
import sys
si = sys.stdin.readline

if __name__ == "__main__":
    while True:
        orders = si().split()
        if len(orders) == 1:
            break

        n, a, b = map(int, orders)
        
        flags = dict()
        cur = 0
        idx = 1
        while True:
            cur = (((a * cur) % n) * (cur % n) + b) % n
            if cur in flags:
                print(n - idx + flags[cur])
                break
            
            flags[cur] = idx
            idx += 1