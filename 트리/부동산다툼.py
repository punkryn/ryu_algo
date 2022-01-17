# https://www.acmicpc.net/problem/20364
import sys
si = sys.stdin.readline

def main():
    n, q = map(int, si().split())
    x = [int(si()) for _ in range(q)]
    bt = [0] * (1 << 20)

    def traverse(x):
        res = 0
        y = x
        while x:
            if bt[x] != 0:
                res = x
            
            x //= 2
        bt[y] = 1
        return res
    
    for t in x:
        tmp = traverse(t)
        print(tmp)
        
        # print(bt[:20])

if __name__ == '__main__':
    main()