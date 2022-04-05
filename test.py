a = [1, 2, 3, 4, 5, 5, 6, 6]
v1, v2 = 0, 0
for v in a:
    if v >= v1:
        tmp = v1
        v1 = v
        if tmp >= v2:
            v2 = tmp
print(v1, v2)