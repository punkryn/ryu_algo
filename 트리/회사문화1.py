# https://www.acmicpc.net/problem/14267
import sys
sys.setrecursionlimit(1000000)
si = sys.stdin.readline
def main():
    n, m = map(int, si().split())
    senior = list(map(int, si().split()))
    tree = [[] for _ in range(n + 1)]
    for i in range(1, n):
        tree[senior[i]].append(i + 1)
    score = [0] * (n + 1)
    # print(tree)

    queries = [list(map(int, si().split())) for _ in range(m)]
    for query in queries:
        i, w = query
        score[i] += w
    
    def dfs(x):
        for nxt in tree[x]:
            score[nxt] += score[x]
            dfs(nxt)
    dfs(1)
            
    print(*score[1:])

if __name__ == '__main__':
    main()