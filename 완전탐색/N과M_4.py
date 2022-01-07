import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(range(1, n + 1))

def go(depth, cur, idx):
    if depth == m:
        for num in cur:
            sys.stdout.write(str(num) + ' ')
        sys.stdout.write('\n')
        return
    
    for i in range(n):
        if i < idx:
            continue

        cur.append(arr[i])
        go(depth + 1, cur, i)
        cur.pop()
go(0, [], 0)