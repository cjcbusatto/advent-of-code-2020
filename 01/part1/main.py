def get_expenses_from_input(input_location):
    f = open(input_location, 'r')
    
    expenses = f.read().split('\n')
    expenses_list_number = []
    for expense in expenses:
        expenses_list_number.append(int(expense))

    expenses_list_number.sort()
    return expenses_list_number

def get_two_expenses_which_sum_2020(expenses):
    counter = 0
    for i,_ in enumerate(expenses):        
        for j,__ in enumerate(expenses):
            counter+=1
            print(f"i={i}, j={j} = {expenses[i] + expenses[j]}")
            if(expenses[i] + expenses[j] > 2020):
                break

            if(expenses[i] + expenses[j] == 2020):
                print(f"Number of comparisons: {counter}")
                return (expenses[i], expenses[j])
    
    return "Error"

expenses = get_expenses_from_input('../input.txt')

value1, value2 = get_two_expenses_which_sum_2020(expenses)
print(f"value1={value1}, value2={value2}")
result = value1 * value2
print(f"value1 x value2 = {result}")