# https://www.acmicpc.net/problem/2729
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(si())):
        n1, n2 = si().split()

        v1 = 0
        for i in range(len(n1) - 1, -1, -1):
            v1 += int(n1[i]) * (2 ** (len(n1) - i - 1))

        v2 = 0
        for i in range(len(n2) - 1, -1, -1):
            v2 += int(n2[i]) * (2 ** (len(n2) - i - 1))
        
        print(bin(v1 + v2)[2:])