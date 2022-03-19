def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1): # 1~cut까지만 자른다
        ap = []
        first = s[:i]
        count = 1
        for j in range(i, len(s), i):
            if first == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    ap.append(str(count))
                    ap.append(first)
                else:
                    ap.append(first)
                first = s[j:j+i]
                count = 1
        if count >= 2:
            ap.append(str(count))
            ap.append(first)
        else:
            ap.append(first)
        # print(ap)
        answer = min(answer, len(''.join(ap)))
    return answer

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))