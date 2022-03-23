# https://www.acmicpc.net/problem/17179
import sys
si = sys.stdin.readline

def main():
    n, m, l = map(int, si().split())
    s = [int(si()) for _ in range(m)]
    q = [int(si()) for _ in range(n)]

    def deter(mid, query):
        cnt = 0
        start = 0
        for i in range(m):
            if s[i] - start >= mid:
                cnt += 1
                start = s[i]
                if cnt == query and l - start >= mid:
                    return False
        return True
        
    for query in q:
        left, right = 1, l
        ans = 0
        while left <= right:
            mid = (left + right) // 2

            if deter(mid, query):
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        print(ans)

if __name__ == '__main__':
    main()