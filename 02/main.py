def get_passwords_from_input(input_location):
    f = open(input_location, 'r')
    
    list_of_passwords = f.read().split('\n')
    f.close()


    passwords = []
    for password in list_of_passwords:
        [policy, letter, password_value] = password.split(" ")
        [low_number, high_number] = policy.split("-")
        
        passwords.append({
            'letter': letter[0],
            'low_number': int(low_number),
            'high_number': int(high_number),
            'value': password_value
        })
        
    return passwords

def is_password_valid_for_part1(password):
    number_of_occurrences = 0
    for char in password['value']:
        if char == password['letter']:
            number_of_occurrences += 1

    if number_of_occurrences >= password['low_number'] and number_of_occurrences <= password['high_number']:
        return True

    return False

def get_number_of_valid_passwords_for_part1(passwords):
    valid_passwords = 0
    for password in passwords:
        if is_password_valid_for_part1(password):
            valid_passwords += 1
    return valid_passwords

def is_password_valid_for_part2(password):
    password_value = password['value']
    policy_letter = password['letter']
    low_number_char = password_value[password['low_number'] - 1]
    high_number_char = password_value[password['high_number'] - 1]

    if low_number_char == policy_letter and high_number_char == policy_letter:
        return False
    
    if low_number_char == policy_letter:
        return True
    if high_number_char == policy_letter:
        return True

def get_number_of_valid_passwords_for_part2(passwords):
    valid_passwords = 0
    for password in passwords:
        if is_password_valid_for_part2(password):
            valid_passwords += 1
    return valid_passwords
passwords = get_passwords_from_input('input')

number_of_valid_passwords_for_part1 = get_number_of_valid_passwords_for_part1(passwords)
number_of_valid_passwords_for_part2 = get_number_of_valid_passwords_for_part2(passwords)
print(f"Part1: Number of valid passwords: {number_of_valid_passwords_for_part1}")
print(f"Part2: Number of valid passwords: {number_of_valid_passwords_for_part2}")
