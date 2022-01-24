import sys

def main():
    n = int(sys.stdin.readline())

    INF = int(1e6)

    maxsum = [0, 0, 0]
    minsum = [INF, INF, INF]
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())

        if i == 0:
            maxsum[0], maxsum[1], maxsum[2] = a, b, c
            minsum[0], minsum[1], minsum[2] = a, b, c
        else:
            tmp = [0, 0, 0]
            tmp[0] = max(maxsum[0] + a, maxsum[1] + a)
            tmp[1] = max(maxsum[0] + b, maxsum[1] + b, maxsum[2] + b)
            tmp[2] = max(maxsum[1] + c, maxsum[2] + c)
            maxsum[0], maxsum[1], maxsum[2] = tmp[0], tmp[1], tmp[2]

            tmp = [0, 0, 0]
            tmp[0] = min(minsum[0] + a, minsum[1] + a)
            tmp[1] = min(minsum[0] + b, minsum[1] + b, minsum[2] + b)
            tmp[2] = min(minsum[1] + c, minsum[2] + c)
            minsum[0], minsum[1], minsum[2] = tmp[0], tmp[1], tmp[2]

    print(max(maxsum), min(minsum))


if __name__ == '__main__':
    main()