# https://www.acmicpc.net/problem/9489
import sys
si = sys.stdin.readline

def main():
    while True:
        n, k = map(int, si().split())
        if n == 0 and k == 0:
            break
        seq = list(map(int, si().split()))
        parents = {0: 0, seq[0]: 0}
        parent = 0
        r = 1
        l = 1
        for i in range(1, n):
            if i == 1:
                l = 1
                continue
            
            if seq[i] - seq[i-1] == 1:
                r += 1
            else:
                for j in range(l, r + 1):
                    parents[seq[j]] = seq[parent]
                parent += 1
                l, r = i, i
        
        for j in range(l, r + 1):
            if parent < len(seq) and j < len(seq):
                parents[seq[j]] = seq[parent]
        
        target = parents[parents[k]]
        ans = 0
        if target != 0:
            for s in seq:
                if s == k: continue
                if parents[k] != parents[s] and parents[parents[s]] == target:
                    ans += 1
        print(ans)

if __name__ == '__main__':
    main()