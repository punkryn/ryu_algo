# https://www.acmicpc.net/problem/16916
import sys
si = sys.stdin.readline

def make_table(p):
    lp = len(p)
    idx = 0
    table = [0] * lp
    for i in range(1, lp):
        while idx > 0 and p[idx] != p[i]:
            idx = table[idx - 1]
        
        if p[idx] == p[i]:
            idx += 1
            table[i] = idx
    return table

def KMP(p, s):
    lp = len(p)
    ls = len(s)

    table = make_table(p)

    j = 0
    for i in range(ls):
        while j and s[i] != p[j]:
            j = table[j - 1]
        
        if s[i] == p[j]:
            if j == lp - 1:
                return 1
            else:
                j += 1
    return 0

if __name__ == '__main__':
    s = si().strip()
    p = si().strip()

    print(KMP(p, s))