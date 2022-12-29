def get_instructions_from_input(input_location):
    f = open(input_location, 'r')

    specifications = f.read().split('\n')
    f.close()

    instruction_set = []
    for specification in specifications:
        instruction, value = specification.split(' ')

        signal = value[0]
        if (signal == '-'):
            counter = -value[1:]
        else:
            counter = value[1:]
        instruction_set.append({
            "instruction": instruction,
            "counter": counter
        })


    return instruction_set
