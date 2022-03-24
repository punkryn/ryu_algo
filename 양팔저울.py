# https://www.acmicpc.net/problem/17610
import sys
import copy
si = sys.stdin.readline

def go(depth, cur):
    global ans
    if depth == 0:
        if int(cur) == 0:
            return
        total = 0
        for i in range(len(cur)):
            if cur[i] == '1':
                total += weights[i]
        
        possible.add(total)
        ans += 1
        return
    
    go(depth - 1, cur + '0')
    go(depth - 1, cur + '1')
    

if __name__ == '__main__':
    k = int(si())
    weights = list(map(int, si().split()))

    possible = set()
    ans = 0
    go(k, '')

    lst = list(possible)
    ans_set = copy.deepcopy(possible)
    for i in range(len(possible) - 1):
        for j in range(i + 1, len(possible)):
            tmp = abs(lst[i] - lst[j])
            if tmp not in ans_set:
                ans += 1
                ans_set.add(tmp)
    print(sum(weights) - ans)