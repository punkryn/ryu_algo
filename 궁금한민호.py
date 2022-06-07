# https://www.acmicpc.net/problem/1507
import sys
si = sys.stdin.readline

INF = int(1e9)

# def find_parent(x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent[x])
#     return parent[x]

# def union(x, y):
#     x = find_parent(x)
#     y = find_parent(y)
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y

if __name__ == '__main__':
    n = int(si())

    matrix = [list(map(int, si().split())) for _ in range(n)]
    # edges = sorted([[matrix[i][j], i, j] for i in range(n) for j in range(i + 1, n)])
    # parent = [i for i in range(n + 1)]
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            tmp = INF
            for k in range(n):
                if k == i or k == j: continue
                tmp = min(tmp, matrix[i][k] + matrix[k][j])
                if matrix[i][j] >= matrix[i][k] + matrix[k][j]:
                    break
            else:
                ans += matrix[i][j]
            
            if tmp < matrix[i][j]:
                print(-1)
                exit()

    # for c, x, y in edges:
    #     if find_parent(x) != find_parent(y):
    #         # print(c, x, y)
    #         union(x, y)
    #         ans += c
    #     else:
    #         tmp = int(1e9)
    #         for k in range(n):
    #             if x == k or y == k: continue
    #             tmp = min(tmp, matrix[x][k] + matrix[k][y])
    #             if c >= matrix[x][k] + matrix[k][y]:
    #                 break
    #         else:
    #             ans += c
    #         if tmp < matrix[x][y]:
    #             print(-1)
    #             exit()
    print(ans)