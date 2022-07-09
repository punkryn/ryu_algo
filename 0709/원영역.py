# https://www.acmicpc.net/problem/10000
import sys
si = sys.stdin.readline

INF = int(1e9)

if __name__ == '__main__':
    n = int(si())
    circles = []
    for _ in range(n):
        x, r = map(int, si().split())
        circles.append((x - r, x + r))
    circles.sort(key=lambda x: (x[0], -x[1]))
    ans = 1
    st = []
    l = []
    for x, y in circles:
        if not st:
            ans += 1
            st.append((x, y))
            l.append(y - x)
            continue
        
        if st[-1][0] <= x < st[-1][1]:
            st.append((x, y))
            l.append(y - x)
            ans += 1
        else:
            tmp = 0
            while st and not (st[-1][0] <= x < st[-1][1]):
                s, e = st.pop()
                tmp = max(tmp, l.pop())
            length = tmp + y - x
            if st and length == st[-1][1] - st[-1][0]:
                ans += 1

            l.append(length)
            ans += 1
            st.append((x, y))
    print(ans)

# 6
# 6 6
# 3 3
# 9 3
# 8 2
# 11 1
# 0 100
# -> 9

# 4
# 9 9
# 3 3
# 9 3
# 15 3
# -> 6

# 7
# 6 6
# 3 3
# 9 3
# 8 2
# 11 1
# 0 100
# 15 3

# 7
# 6 6
# 3 3
# 9 3
# 8 2
# 11 1
# 9 9
# 15 3