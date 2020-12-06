def get_expenses_from_input(input_location):
    f = open(input_location, 'r')
    
    expenses = f.read().split('\n')
    expenses_list_number = []
    for expense in expenses:
        expenses_list_number.append(int(expense))

    expenses_list_number.sort()
    return expenses_list_number

def get_three_expenses_which_sum_2020(expenses):
    counter = 0
    for i,_ in enumerate(expenses):        
        for j,__ in enumerate(expenses):
            for k,___ in enumerate(expenses):
                counter += 1
                if(expenses[i] + expenses[j] + expenses[k] > 2020):
                    break

                if(expenses[i] + expenses[j] + expenses[k] == 2020):
                    print(f"Number of comparisons: {counter}")
                    return (expenses[i], expenses[j], expenses[k])
    
    return "Error"

expenses = get_expenses_from_input('../input.txt')

value1, value2, value3 = get_three_expenses_which_sum_2020(expenses)
print(f"value1={value1}, value2={value2}, value3={value3}")
result = value1 * value2 * value3
print(f"value1 x value2 x value3 = {result}")