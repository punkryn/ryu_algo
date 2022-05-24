# https://www.acmicpc.net/problem/2800
import sys
from itertools import combinations
si = sys.stdin.readline

def go(depth, cnt):
    if depth == m:
        if not cnt:
            return
        tmp = ''
        for i in range(n):
            if not check[i]:
                tmp += s[i]
        ans.add(tmp)
        return
    
    check[seq[depth][0]] = True
    check[seq[depth][1]] = True
    go(depth + 1, cnt + 1)
    check[seq[depth][0]] = False
    check[seq[depth][1]] = False

    go(depth + 1, cnt)

if __name__ == '__main__':
    s = si().rstrip()
    n = len(s)

    st = []
    seq = []
    for i in range(n):
        if s[i] == '(':
            st.append(i)
        elif s[i] == ')':
            idx = st.pop()
            seq.append((idx, i))
    
    m = len(seq)
    ans = set()
    check = [False] * n
    go(0, 0)
    for a in sorted(list(ans)):
        print(a)