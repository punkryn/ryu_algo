from bisect import bisect_left, bisect_right

a = [1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7,7,7,7,7,7,9,10]

print(bisect_left(a, 1), bisect_right(a, 1))

def lower_bound(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

def upper_bound(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end

print(lower_bound(a, 1), upper_bound(a, 1))