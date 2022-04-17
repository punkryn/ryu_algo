# https://www.acmicpc.net/problem/1043
import sys
si = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    n, m = map(int, si().split())
    truth = list(map(int, si().split()))


    party = [[] for _ in range(m)]
    parent = [i for i in range(n + 1)]

    for i in range(1, truth[0]):
        if find_parent(truth[i]) != find_parent(truth[i + 1]):
            union(truth[i], truth[i + 1])

    if truth[0] == 0:
        tmp = [list(map(int, si().split())) for _ in range(m)]
        print(m)
        exit()

    for i in range(m):
        member = list(map(int, si().split()))
        for j in range(1, member[0] + 1):
            party[i].append(member[j])

        for j in range(1, member[0]):
            if find_parent(member[j]) != find_parent(member[j + 1]):
                union(member[j], member[j + 1])
                
    
    comp = find_parent(truth[1])
    ans = m
    for p in party:
        for member in p:
            if find_parent(member) == comp:
                ans -= 1
                break
    print(ans)