# https://www.acmicpc.net/problem/9342
import sys
import re
si = sys.stdin.readline

if __name__ == '__main__':
    reg = '[ABCDEF]?A+F+C+[ABCDEF]?'
    res = re.compile(reg)
    for _ in range(int(si())):
        string = si().strip()
        if res.fullmatch(string):
            print('Infected!')
        else:
            print('Good')