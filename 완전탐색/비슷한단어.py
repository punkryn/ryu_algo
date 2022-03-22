# https://www.acmicpc.net/problem/1411
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    words = [si().strip() for _ in range(n)]

    ans = 0

    def isShome(arr):
        conv = dict()
        tmp = set()
        for i in range(len(arr[0])):
            if arr[0][i] not in conv:
                if arr[1][i] in tmp:
                    return False
                conv[arr[0][i]] = arr[1][i]
                tmp.add(arr[1][i])
            else:
                if conv[arr[0][i]] != arr[1][i]:
                    return False

        return True

    def comb(prev, depth, cur):
        nonlocal ans
        if depth == 0:
            if isShome(cur):
                ans += 1
            return
        
        for i in range(prev + 1, n - depth + 1):
            cur.append(words[i])
            comb(i, depth - 1, cur)
            cur.pop()
    
    comb(-1, 2, [])
    print(ans)

if __name__ == '__main__':
    main()