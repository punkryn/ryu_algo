# https://www.acmicpc.net/problem/1991
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    tree = {}
    for _ in range(n):
        node, left, right = si().strip().split()
        # if node not in tree:
        tree[node] = [left, right]

    def preorder(x):
        if x == '.':
            return
        
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])
    
    def inorder(x):
        if x == '.':
            return
        
        inorder(tree[x][0])
        print(x, end='')
        inorder(tree[x][1])

    def postorder(x):
        if x == '.':
            return
        
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end='')
    
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')

if __name__ == '__main__':
    main()