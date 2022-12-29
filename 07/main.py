def get_groups_from_input(input_location):
    f = open(input_location, 'r')

    specifications = f.read().split('\n')
    f.close()

    bags_dic = {}
    for specification in specifications:
        bag_color, contains = specification.split('contain ')

        different_bags = contains.split(', ')

        nodes = {}
        for bag in different_bags:
            if bag != 'no other bags.':
                nodes[bag[2:].replace(".", "").replace(
                    "bags", "").replace("bag", "").strip()] = bag[0]
        bags_dic[bag_color.replace("bags", "").strip()] = nodes

    return bags_dic


def search_shiny_bags(bags):
    answer = set()

    def search(color):
        for b in bags:
            if color in bags[b]:
                answer.add(b)
                search(b)

    search('shiny gold')

    return answer
def part2():
    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = int(bags[bag][s])

            count += multiplier * search(s)
        return count
    return search('shiny gold' ) - 1

bags = get_groups_from_input('input')
found = search_shiny_bags(bags)
print(len(found))
print(part2())
# bags_with_shiny_directly = get_bags_carrying_color(bags, 'shiny')

# find_transitive_bags_which_can_reach_shiny_bag(bags, bags_with_shiny_directly)
