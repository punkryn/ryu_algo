# https://www.acmicpc.net/problem/17298
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    a = list(mis())
    
    st = []
    ans = []
    for i in range(n - 1, -1, -1):
        if not st:
            ans.append(-1)
            st.append(a[i])
        else:
            while st and st[-1] <= a[i]:
                st.pop()
            
            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])
            st.append(a[i])
    
    print(*ans[::-1])