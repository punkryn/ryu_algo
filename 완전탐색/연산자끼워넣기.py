import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))

def go(depth, res, ans):
    if depth == n:
        # print(res)
        if res > ans[0]:
            ans[0] = res
        if res < ans[1]:
            ans[1] = res
        return
    
    if ops[0] > 0:
        ops[0] -= 1
        go(depth + 1, res + num[depth], ans)
        ops[0] += 1
    
    if ops[1] > 0:
        ops[1] -= 1
        go(depth + 1, res - num[depth], ans)
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        go(depth + 1, res * num[depth], ans)
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        if res < 0:
            tmp = -(-res // num[depth])
            go(depth + 1, tmp, ans)
        else:
            go(depth + 1, res // num[depth], ans)
        ops[3] += 1
    
ans = [-1e9, 1e9]
go(1, num[0], ans)
print(ans[0])
print(ans[1])