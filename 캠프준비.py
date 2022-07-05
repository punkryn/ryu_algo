# https://www.acmicpc.net/problem/16938
import sys
from itertools import combinations
si = sys.stdin.readline

if __name__ == '__main__':
    n, l, r, x = map(int, si().split())
    a = sorted(list(map(int, si().split())))
    print(sum([1 for i in range(1, n + 1) for comb in combinations(a, i) if l <= sum(comb) <= r and comb[-1] - comb[0] >= x]))