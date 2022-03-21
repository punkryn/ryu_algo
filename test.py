import math

ans = []
for i in range(2, 1000):
    for j in range(1, int(math.sqrt(i)) + 1):
        if j == 1: continue
        if i % j == 0:
            break
    else:
        ans.append(i)
print(ans)