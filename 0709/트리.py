# https://www.acmicpc.net/problem/4256
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

root = 0
def post(left, right, preorder, inorder):
    global root
    if left > right:
        return []

    if left == right:
        root += 1
        return [inorder[right]]
    
    root_idx = inorder.index(preorder[root])
    root += 1
    return post(left, root_idx - 1, preorder, inorder) + post(root_idx + 1, right, preorder, inorder) + [inorder[root_idx]]

def main():
    global root
    n = int(si())
    preorder = list(mis())
    inorder = list(mis())
    root = 0
    print(*post(0, n - 1, preorder, inorder))

if __name__ == '__main__':
    for _ in range(int(si())):
        main()