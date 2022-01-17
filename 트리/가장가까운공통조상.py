# https://www.acmicpc.net/problem/3584
import sys
si = sys.stdin.readline
sys.setrecursionlimit(100000)

def main():
    n = int(si())
    # tree = [[] for _ in range(n + 1)]
    rev_tree = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, si().split())
        rev_tree[b] = a
    n1, n2 = map(int, si().split())
    visited = [0] * (n + 1)

    while n1:
        visited[n1] = 1
        n1 = rev_tree[n1]
    
    while not visited[n2] and n2:
        n2 = rev_tree[n2]
    print(n2)

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()