# https://www.acmicpc.net/problem/2469
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    k = int(si())
    n = int(si())
    result = si().strip()
    
    ladder = [si().strip() for _ in range(n)]
    