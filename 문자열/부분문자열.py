# https://www.acmicpc.net/problem/16916
import sys
si = sys.stdin.readline

def make_table(p):
    lp = len(p)
    table = [0] * lp
    i = 0
    for j in range(1, lp):
        while i and p[i] != p[j]:
            i = table[i - 1]
        
        if p[i] == p[j]:
            i += 1
            table[j] = i
    return table

def KMP(p, s):
    lp = len(p)
    ls = len(s)
    i = 0

    table = make_table(p)

    for j in range(ls):
        while i and p[i] != s[j]:
            i = table[i - 1]
        
        if p[i] == s[j]:
            if i == lp - 1:
                return 1
            else:
                i += 1
    return 0

if __name__ == '__main__':
    s = si().strip()
    p = si().strip()

    print(KMP(p, s))