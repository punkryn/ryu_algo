# https://www.acmicpc.net/problem/3986

import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    ans = 0
    for _ in range(n):
        string = si().strip()
        st = []
        for w in string:
            if not st:
                st.append(w)
            else:
                if st[-1] == w:
                    st.pop()
                else:
                    st.append(w)
        if not st:
            ans += 1
    print(ans)