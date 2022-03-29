a = [(1, 2), (1, 3)]
print(min(a, key=lambda x: (x[0], x[1])))