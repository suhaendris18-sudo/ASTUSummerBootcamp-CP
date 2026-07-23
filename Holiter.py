n = int(input())
s = input()
rooms = [0] * 10

for room in s:
    if room == "L":
        for i in range(10):
            if rooms[i] == 0:
                rooms[i] = 1
                break

    elif room == "R":
        for i in range(9, -1, -1):
            if rooms[i] == 0:
                rooms[i] = 1
                break

    else:
        rooms[int(room)] = 0

print("".join(map(str, rooms)))
