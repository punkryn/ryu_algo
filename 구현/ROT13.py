# https://www.acmicpc.net/problem/4446
import sys
si = sys.stdin.readline

if __name__ == "__main__":
    mo = ['a', 'i', 'y', 'e', 'o', 'u']
    ja = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
    
    while True:
        try:
            string = input()
            
            ans = ''
            for s in string:
                s_ori = s
                s = s.lower()
                if s in mo:
                    nxt = mo[(mo.index(s) - 3) % 6]
                    if s_ori == s:
                        ans += nxt
                    else:
                        ans += nxt.upper()
                elif s in ja:
                    nxt = ja[(ja.index(s) + 10) % 20]
                    if s_ori == s:
                        ans += nxt
                    else:
                        ans += nxt.upper()
                else:
                    ans += s_ori
            print(ans)
        except:
            break