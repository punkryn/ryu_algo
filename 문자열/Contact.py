# https://www.acmicpc.net/problem/1013
import sys
import re
si = sys.stdin.readline

if __name__ == '__main__':
    reg = '^(100+1+|01)+$'
    for _ in range(int(si())):
        pattern = si().strip()
        if re.compile(reg).match(pattern):
            print('YES')
        else:
            print('NO')