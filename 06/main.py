def get_groups_from_input(input_location):
    f = open(input_location, 'r')

    groups = f.read().replace('\n', ' ').split('  ')
    f.close()
    return groups


def get_counter_for_part1(groups):
    counter = 0
    for group in groups:
        answers_set = set()
        for answer in group:
            if answer == ' ':
                continue
            answers_set.add(answer)

        counter += len(answers_set)
    return counter


def get_counter_for_part2(groups):
    counter = 0
    for group in groups:
        person = 1
        answers_dic = {}
        for answer in group:
            if answer == ' ':
                person += 1
                continue

            if answers_dic.get(answer):
                answers_dic[answer] += 1
            else:
                answers_dic[answer] = 1
        print(f"Dic: {answers_dic}")
        print(f"Person: {person}")

        for (key,value) in answers_dic.items():
            if value == person:
                counter+=1

    return counter


groups = get_groups_from_input('input')

counter = get_counter_for_part1(groups)
counter = get_counter_for_part2(groups)
print(counter)
