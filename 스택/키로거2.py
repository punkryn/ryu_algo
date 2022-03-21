# https://www.acmicpc.net/problem/5397
# 1
# -d>a<<<<<a>>>>>b<pq<<<z--
# aapqb
import sys
si = sys.stdin.readline

def main():
    string = si().strip()
    st1 = []
    st2 = []
    for s in string:
        if s == '<':
            if st1:
                st2.append(st1.pop())
        elif s == '>':
            if st2:
                st1.append(st2.pop())
        elif s == '-':
            if st1:
                st1.pop()
        else:
            st1.append(s)
    
    st2.reverse()
    print(''.join(st1 + st2))

if __name__ == '__main__':
    for _ in range(int(si())):
        main()