# https://www.acmicpc.net/problem/4659
import sys
import re
si = sys.stdin.readline

mo = ['a', 'e', 'i', 'o', 'u']
ja = 'bcdfghjklmnpqrstwxyz'
ok = 'acceptable'

def isStrict(word):
    mcnt = 0
    jcnt = 0
    for w in word:
        if w in mo:
            mcnt += 1
            jcnt = 0
        elif w in ja:
            jcnt += 1
            mcnt = 0
        else:
            mcnt = 0
            jcnt = 0
        if mcnt == 3 or jcnt == 3:
            return True
    return False

def isStrict2(word):
    cnt = 0
    cur = ''
    for w in word:
        if w == 'e' or w == 'o':
            cur = ''
            cnt = 0
            continue
        if cur != w:
            cur = w
            cnt = 0
        cnt += 1
        if cnt == 2:
            return True
    return False

if __name__ == "__main__":
    reg1 = '\w*[aeiou]\w*'
    reg2 = '\w*'
    c = re.compile(reg1)
    
    while True:
        word = si().strip()
        if word == 'end': break

        if not c.search(word):
            print(f'<{word}> is not {ok}.')
            continue

        if isStrict(word):
            print(f'<{word}> is not {ok}.')
            continue

        if isStrict2(word):
            print(f'<{word}> is not {ok}.')
            continue
        
        print(f'<{word}> is {ok}.')