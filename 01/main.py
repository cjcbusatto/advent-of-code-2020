def get_expenses_from_input(input_location):
    f = open(input_location, 'r')
    
    expenses = f.read().split('\n')
    expenses_list_number = []
    for expense in expenses:
        expenses_list_number.append(int(expense))

    expenses_list_number.sort()
    return expenses_list_number

def get_two_expenses_which_sum_2020(expenses):
    for i, _ in enumerate(expenses):        
        for j, __ in enumerate(expenses):
            inverted_index = len(expenses) - j - 1
            if(expenses[i] + expenses[inverted_index] > 2020):
                continue

            if(expenses[i] + expenses[inverted_index] == 2020):
                return (expenses[i], expenses[inverted_index])
    
    return "Error"

expenses = get_expenses_from_input('input.txt')

value1,value2 = get_two_expenses_which_sum_2020(expenses)
result = value1 * value2
print(result)