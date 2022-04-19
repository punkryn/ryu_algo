# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline

def traverse(st1, ed1, st2, ed2):
    if st1 > ed1 or st2 > ed2:
        return

    root_idx = inorder_idx[postorder[ed2]]
    left_size = root_idx - st1
    print(postorder[ed2], end=' ')

    traverse(st1, root_idx - 1, st2, st2 + left_size - 1)
    traverse(root_idx + 1, ed1, st2 + left_size, ed2 - 1)

if __name__ == "__main__":
    n = int(si())
    inorder = list(map(int, si().split()))
    postorder = list(map(int, si().split()))
    inorder_idx = [0] * (n + 1)
    for i in range(n):
        inorder_idx[inorder[i]] = i
    traverse(0, n - 1, 0, n - 1)