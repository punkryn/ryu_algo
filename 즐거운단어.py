# https://www.acmicpc.net/problem/2922
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(depth, m_, j_, cnt, l):
    global ans, flag
    if m_ >= 3 or j_ >= 3:
        return

    if depth >= n:
        if flag or l:
            ans += cnt
        return
    
    idx = depth
    for i in range(depth, n):
        if s[i] == '_':
            idx = i
            break
            
        if s[i] in ['A', 'E', 'I', 'O', 'U']:
            m_ += 1
            j_ = 0
        else:
            j_ += 1
            m_ = 0
            if s[i] == 'L':
                flag = True
    
    if idx == depth and s[idx] != '_':
        if s[idx] in ['A', 'E', 'I', 'O', 'U']:
            go(idx + 1, m_, 0, cnt, l)
        else:
            if s[idx] == 'L':
                go(idx + 1, 0, j_, cnt, True)
            else:
                go(idx + 1, 0, j_, cnt, l)
        return

    go(idx + 1, m_ + 1, 0, cnt * 5, l)
    go(idx + 1, 0, j_ + 1, cnt * 20, l)

    l = True
    go(idx + 1, 0, j_ + 1, cnt, l)
    l = False
    

if __name__ == '__main__':
    s = list(si().strip())
    n = len(s)

    if '_' not in s and 'L' in s:
        m = j = 0
        for i in range(n):
            if s[i] in ['A', 'E', 'I', 'O', 'U']:
                m += 1
                j = 0
            else:
                j += 1
                m = 0
            
            if m >= 3 or j >= 3:
                print(0)
                break
        else:
            print(1)
        exit()
    
    ans = 0
    flag = False
    
    go(0, 0, 0, 1, False)
    print(ans)