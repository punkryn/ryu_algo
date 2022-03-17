# https://www.acmicpc.net/problem/1990
import sys
import math
si = sys.stdin.readline

def isPrime(x):
    if 2 <= x <= 3:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    x = str(x)
    l, r = 0, len(x) - 1
    while l <= r:
        if x[l] != x[r]:
            return False
        
        l += 1
        r -= 1
    return True

def main():
    a, b = map(int, si().split())
    if a % 2 == 0:
        a += 1
    
    for i in range(a, b + 1, 2):
        if not isPalindrome(i):
            continue

        if not isPrime(i):
            continue

        print(i)
    
    print(-1)

if __name__ == '__main__':
    main()