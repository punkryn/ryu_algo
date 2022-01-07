import sys
n, m = map(int, sys.stdin.readline().split(' '))
nums = sorted(list(map(int, sys.stdin.readline().split(' '))))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for s in selected:
            sys.stdout.write(str(s) + ' ')
        sys.stdout.write('\n')
        return
    
    prev = 0
    for i in range(n):
        if used[i] == 1 or prev == nums[i]:
            continue

        prev = nums[i]
        used[i] = 1
        selected[k] = nums[i]
        rec_func(k + 1)
        selected[k] = 0
        used[i] = 0

rec_func(0)