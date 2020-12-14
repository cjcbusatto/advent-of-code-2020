def get_map_from_input(input_location):
    f = open(input_location, 'r')

    input_map = f.read().split('\n')
    f.close()

    lines = len(input_map)
    columns = len(input_map[0])

    print(f"Original map = {lines} x {columns}")

    extended_map = []
    for line in input_map:
        extended_map.append(line * 200)

    print(
        f"Extended map = {str(len(extended_map))} x {str(len(extended_map[0]))}")

    return extended_map


def traverse_map_counting_trees(extended_map, right, down):

    squares = []
    i = 0
    j = 0
    while i < len(extended_map):

        if i == 0:
            squares.append(extended_map[i][j])
        else:
            try:
                squares.append(extended_map[i][(j * right)])
            except:
                print("Error")
                break

        i += down
        j+= 1

    tree_counter = 0
    for char in squares:
        if char == '#':
            tree_counter += 1
    return tree_counter


extended_map = get_map_from_input('input')

number_of_threes = traverse_map_counting_trees(extended_map, 1, 1)
print(f"1x1 => {number_of_threes}")

number_of_threes = traverse_map_counting_trees(extended_map, 3, 1)
print(f"3x1 => {number_of_threes}")

number_of_threes = traverse_map_counting_trees(extended_map, 5, 1)
print(f"5x1 => {number_of_threes}")

number_of_threes = traverse_map_counting_trees(extended_map, 7, 1)
print(f"7x1 => {number_of_threes}")

number_of_threes = traverse_map_counting_trees(extended_map, 1, 2)
print(f"1x2 => {number_of_threes}")

total = traverse_map_counting_trees(extended_map, 1, 1) * traverse_map_counting_trees(extended_map, 3, 1) * traverse_map_counting_trees(
    extended_map, 5, 1) * traverse_map_counting_trees(extended_map, 7, 1) * traverse_map_counting_trees(extended_map, 1, 2)

print(f"Numbers multiplied = {total}")