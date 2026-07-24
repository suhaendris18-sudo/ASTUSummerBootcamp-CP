t = int(input())

for i in range(t):
    n = int(input())

    first = input().split()
    second = input().split()
    third = input().split()

    words = {}

    for x in first:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1

    for x in second:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1

    for x in third:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1

    score1 = 0
    score2 = 0
    score3 = 0

    for x in first:
        if words[x] == 1:
            score1 += 3
        elif words[x] == 2:
            score1 += 1

    for x in second:
        if words[x] == 1:
            score2 += 3
        elif words[x] == 2:
            score2 += 1

    for x in third:
        if words[x] == 1:
            score3 += 3
        elif words[x] == 2:
            score3 += 1

    print(score1, score2, score3)
