# https://www.acmicpc.net/problem/6137
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    words = [si().strip() for _ in range(n)]

    l, r = 0, n - 1
    ans = ''
    while l <= r:
        if l == r:
            ans += words[l]
            break
        if ord(words[l]) < ord(words[r]):
            ans += words[l]
            l += 1
        elif ord(words[l]) > ord(words[r]):
            ans += words[r]
            r -= 1
        else:
            l_, r_ = l + 1, r - 1
            if l_ >= r_:
                ans += words[l]
                l += 1
                continue
            flag = False
            while l_ < r_:
                if words[l_] < words[r_]:
                    ans += words[l]
                    l += 1
                    flag = True
                    break
                elif words[r_] < words[l_]:
                    ans += words[r]
                    r -= 1
                    flag = True
                    break
                elif words[r_] == words[l_] and words[r_] > words[r]:
                    ans += words[l]
                    ans += words[r]
                    l += 1
                    r -= 1
                    flag = True
                    break
                    
                l_ += 1
                r_ -= 1
            if not flag:
                ans += words[l]
                l += 1
                                        
    for i in range(1, n + 1):
        print(ans[i - 1], end='')
        if i % 80 == 0:
            print()