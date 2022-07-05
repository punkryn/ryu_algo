struct = {
    ' ': 36, '$': 37, '%': 38, '*': 39, '+': 40, '-': 41, '.': 42, '/': 43, ':': 44,
}

def bottom_up(x, y, qr):
    tmp = ''
    for i in range(x, x - 4, -1):
        for j in range(y, y - 2, -1):
            tmp += qr[i][j]
    return tmp

def top_down(x, y, qr):
    tmp = ''
    for i in range(x, x + 4):
        for j in range(y, y - 2, -1):
            tmp += qr[i][j]
    return tmp

def rot1(x, y, qr):
    tmp = ''
    for i in range(x, x - 2, -1):
        for j in range(y, y - 2, -1):
            tmp += qr[i][j]

    for i in range(x - 1, x + 1):
        for j in range(y - 2, y - 4, -1):
            tmp += qr[i][j]
    return tmp

def rot2(x, y, qr):
    tmp = ''
    for i in range(x, x + 2):
        for j in range(y, y - 2, -1):
            tmp += qr[i][j]
    for i in range(x + 1, x - 1, -1):
        for j in range(y - 2, y - 4, -1):
            tmp += qr[i][j]
    return tmp

def toBin(n):
    n = str(bin(n))[2:]
    while len(n) < 8:
        n = '0' + n
    return n

def solution(qr):
    answer = []

    for i in range(10, 36):
        struct[chr(ord('A') + i - 10)] = i

    rev = dict()
    for key in struct:
        rev[toBin(struct[key])] = key

    for i in range(10):
        rev[toBin(i)] = str(i)

    data = []
    for i in range(1, 21):
        # 1
        if i == 1:
            data.append(bottom_up(14, 20, qr))
        elif i == 2:
            data.append(rot1(10, 20, qr))
        elif i == 3:
            data.append(top_down(11, 18, qr))
        elif i == 4:
            data.append(top_down(15, 18, qr))
        elif i == 5:
            data.append(rot2(19, 18, qr))
        elif i == 6:
            data.append(bottom_up(18, 16, qr))
        elif i == 7:
            data.append(bottom_up(14, 16, qr))
        elif i == 8:
            data.append(rot1(10, 16, qr))
        elif i == 9:
            data.append(top_down(11, 14, qr))
        elif i == 10:
            data.append(top_down(15, 14, qr))
        elif i == 11:
            data.append(rot2(19, 14, qr))
        elif i == 12:
            data.append(bottom_up(18, 12, qr))
        elif i == 13:
            data.append(bottom_up(14, 12, qr))
        elif i == 14:
            data.append(bottom_up(10, 12, qr))
        elif i == 15:
            data.append(bottom_up(5, 12, qr))
        elif i == 16:
            data.append(rot1(1, 12, qr))
        elif i == 17:
            data.append(top_down(2, 10, qr))
        elif i == 18:
            data.append(top_down(7, 10, qr))
        elif i == 19:
            data.append(top_down(11, 10, qr))
        elif i == 20:
            data.append(top_down(15, 10, qr))
    print(data)
    word = ''
    for b in data:
        if rev[b] == '0':
            continue
        word += rev[b]
    print(word)

    tmp2 = ''
    tmp = bottom_up(12, 8, qr)
    tmp2 += rev['0000' + tmp[4:]] + rev['0000' + tmp[:4]]
    tmp = top_down(9, 5, qr)
    tmp2 += rev['0000' + tmp[4:]] + rev['0000' + tmp[:4]]
    tmp = bottom_up(12, 3, qr)
    tmp2 += rev['0000' + tmp[4:]] + rev['0000' + tmp[:4]]
    tmp = top_down(9, 1, qr)
    tmp2 += rev['0000' + tmp[4:]] + rev['0000' + tmp[:4]]
    print(tmp)
    return [word, '0x' + tmp2]