# https://www.acmicpc.net/problem/1802
import sys
si = sys.stdin.readline

def dnq(start, end, s):
    if start == end:
        return True
    l, r = start, end
    mid = (start + end) // 2
    while l < r:
        if s[l] == s[r]:
            return False
        l += 1
        r -= 1
    
    return dnq(start, mid - 1, s) and dnq(mid + 1, end, s)

def main():
    s = si().strip()
    l, r = 0, len(s) - 1
    print('YES' if dnq(l, r, s) else 'NO')

if __name__ == '__main__':
    for _ in range(int(si())):
        main()