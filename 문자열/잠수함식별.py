# https://www.acmicpc.net/problem/2671
import sys
import re

si = sys.stdin.readline

if __name__ == '__main__':
    pattern = si().strip()
    reg = '^((100+1+)|(01))+$'
    if re.compile(reg).match(pattern):
        print('SUBMARINE')
    else:
        print('NOISE')