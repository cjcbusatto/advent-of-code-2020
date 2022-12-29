def get_boardings_from_input(input_location):
    f = open(input_location, 'r')

    boardings = f.read().split('\n')

    return boardings


boardings = get_boardings_from_input('input')
print(boardings)


max_id = 0
list_ids = []
for boarding in boardings:
    upper_position = 127
    lower_position = 0

    half = -1
    print(boarding[:-3])
    for index, char in enumerate(boarding[:-3]):

        if index == (len(boarding[:-3]) - 1):
            if char == 'F':
                half = lower_position
                continue
            if char == 'B':
                half = upper_position
                continue
        if char == 'F':
            upper_position = int((upper_position + lower_position) / 2)

        if char == 'B':
            lower_position = int((upper_position + lower_position) / 2) + 1

    if half == -1:
        exit("error on half")

    seat = boarding[-3:]

    upper_position = 7
    lower_position = 0
    seat_position = -1

    for index, char in enumerate(seat):
        if index == len(seat) - 1:
            if char == 'R':
                seat_position = upper_position
                continue
            if char == 'L':
                seat_position = lower_position
                continue

        if char == 'L':
            upper_position = int((upper_position + lower_position) / 2)

        if char == 'R':
            lower_position = int((upper_position + lower_position) / 2) + 1

        print(f"[{lower_position}, {upper_position}]")

    if seat_position == -1:
        exit("error on seat position")

    print(f"half = {half}, seat_position = {seat_position}")

    res = half * 8 + seat_position
    list_ids.append(res)
    print(f"Boarding = {res}")
    if res > max_id:
        max_id = res

list_ids.sort()


index = 1
while True:
    if (list_ids[index] - 1) in list_ids and list_ids[index] + 1 in list_ids:
        index += 1
        continue

    print("#")
    print(list_ids[index-1])
    print(list_ids[index])
    print(list_ids[index+1])
    print("#")
    index += 1
