# https://www.acmicpc.net/problem/9996
import re
import sys

si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    pattern = si().strip().replace('*', '[a-z]*')
    comp = re.compile(pattern)
    for _ in range(n):
        file_name = si().strip()
        if comp.fullmatch(file_name):
            print('DA')
        else:
            print('NE')