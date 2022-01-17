a = [5, 28, 24, 45, 30, 60, 52, 98, 50]

def posttopre(l, r):
    if l > r: return
    mid = l
    for i in range(r-1, l-1, -1):
        if a[i] < a[r]:
            mid = i + 1
            break
    
    print(a[r])
    posttopre(l, mid-1)
    posttopre(mid, r-1)
posttopre(0, len(a)-1)