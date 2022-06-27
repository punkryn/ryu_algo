# https://www.acmicpc.net/problem/1874
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = [int(si()) for _ in range(n)]
    st = []
    idx = 0
    ans = []
    for i in range(1, n + 1):
        if i <= a[idx]:
            st.append(i)
            ans.append('+')
        
        while st and st[-1] == a[idx]:
            ans.append('-')
            st.pop()
            idx += 1
    if st:
        print('NO')
    else:
        print('\n'.join(ans))