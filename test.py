def solution(n, works):
    answer = 0
    
    total = sum(works) - n
    if total <= 0:
        return 0
    
    cnt = n
    while cnt:
        a, b = 0, 0
        ai, bi = -1, -1
        for i, work in enumerate(works):
            if work > a:
                a = work
                ai = i
            else:
                if work > b:
                    b = work
                    bi = i
        print(a, b,ai, bi)
        if abs(a - b) > cnt:
            if a > b:
                works[ai] = a - cnt
            else:
                works[bi] = b - cnt
            cnt = 0
        else:
            if a > b:
                gap = a - b
                works[ai] -= gap
                cnt -= gap
            elif a < b:
                gap = b - a
                works[bi] -= gap
                cnt -= gap
            else:
                if cnt >= 2:
                    works[ai] -= 1
                    works[bi] -= 1
                    cnt -= 2
                else:
                    works[ai] -= 1
                    cnt -= 1
    print(works)
    return answer
works = [2,1,2]
n = 1
solution(n, works)