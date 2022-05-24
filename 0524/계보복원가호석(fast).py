input = __import__('sys').stdin.readline

n = int(input())
names = input().split()
indices = dict(zip(names, range(n)))
m = int(input())

ances = [[] for i in range(n)]
descen = [[] for i in range(n)]
for i in range(m):
    a, b = input().split()
    a = indices[a]
    b = indices[b]
    ances[a].append(b)
    descen[b].append(a)

print(n - sum(map(bool, ances)))
roots = sorted(names[i] for i in range(n) if not ances[i])
print(*roots)

for name in sorted(names):
    i = indices[name]
    acnt = len(ances[i])
    son = [x for x in descen[i] if len(ances[x]) == acnt+1]
    son = sorted(names[i] for i in son)
    print(name, len(son), *son)