# https://www.acmicpc.net/problem/20114
import sys
si = sys.stdin.readline

def main():
    n, h, w = map(int, si().split())
    strs = [si().strip() for _ in range(h)]
    start = 0
    ans = ''
    while start < n * w:
        flag = False
        for string in strs:
            for word in string[start:start+w]:
                if flag:
                    break
                if word == '?':
                    continue
                ans += word
                flag = True
        
        if not flag:
            ans += '?'
        start += w
    print(ans)

if __name__ == '__main__':
    main()