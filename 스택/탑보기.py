# https://www.acmicpc.net/problem/22866
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    heights = list(map(int, si().split()))
    st1 = [(heights[0], 0)]
    st2 = [(heights[-1], n - 1)]
    ans = [[0, -1] for _ in range(n)]
    for i in range(1, n):
        while st1 and st1[-1][0] <= heights[i]:
            st1.pop()
        ans[i][0] += len(st1)
        if st1:
            ans[i][1] = st1[-1][1]
        st1.append((heights[i], i))
    
    for i in range(n - 2, -1, -1):
        while st2 and st2[-1][0] <= heights[i]:
            st2.pop()
        ans[i][0] += len(st2)
        if st2:
            ans[i][1] = st2[-1][1] if ans[i][1] == -1 else min(st2[-1][1], ans[i][1], key=lambda x: (abs(x - i), x))
        st2.append((heights[i], i))
    
    for a in ans:
        cnt, idx = a
        if cnt == 0:
            print(cnt)
        else:
            print(cnt, idx + 1)

if __name__ == '__main__':
    main()