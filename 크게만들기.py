# https://www.acmicpc.net/problem/2812
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    num = si().strip()
    st = []
    k_ = k
    for w in num:
        w = int(w)
        if not st:
            st.append(w)
        else:
            while st and st[-1] < w and k:
                st.pop()
                k -= 1
            st.append(w)
    print(''.join(map(str, st[:n - k_])))