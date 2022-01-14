# https://www.acmicpc.net/problem/2606
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    pair = int(si())
    network = [[] for _ in range(n + 1)]
    for _ in range(pair):
        a, b = map(int, si().split())
        network[a].append(b)
        network[b].append(a)
    
    visited = [0] * (n + 1)
    def dfs(x):
        visited[x] = 1
        cnt = 1
        for nxt in network[x]:
            if visited[nxt] != 0: continue
            cnt += dfs(nxt)
        return cnt
    print(dfs(1) - 1)

if __name__ == '__main__':
    main()