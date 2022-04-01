from itertools import permutations

tmp = list(permutations(list(range(1, 7)), 4))
cnt = 0
for per in tmp:
    if 5 in per and 6 in per:
        cnt += 1
print(cnt)
print(len(tmp))