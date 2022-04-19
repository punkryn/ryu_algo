# https://www.acmicpc.net/problem/1786
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

def KMP(t, p):
    lt = len(t)
    lp = len(p)
    table = make_table(p)
    i = 0
    ans = []
    for j in range(lt):
        while i and t[j] != p[i]:
            i = table[i - 1]
        
        if t[j] == p[i]:
            if i == lp - 1:
                ans.append(j - lp + 2)
                i = table[i]
            else:
                i += 1
    return ans

if __name__ == '__main__':
    t = si().rstrip()
    p = si().rstrip()

    pos = KMP(t, p)
    print(len(pos))
    print(*pos)