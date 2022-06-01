# https://www.acmicpc.net/problem/1918
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    s = si().strip()
    order = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1}
    ans = ''
    stack = []
    for w in s:
        if 'A' <= w <= 'Z':
            ans += w
        elif w == '(':
            stack.append(w)
        elif w == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            if not stack:
                stack.append(w)
            else:
                while stack and order[stack[-1]] >= order[w]:
                    ans += stack.pop()
                stack.append(w)
    
    while stack:
        ans += stack.pop()
    print(ans)