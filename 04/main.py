def get_passports_from_input(input_location):
    f = open(input_location, 'r')

    passports = f.read().split('\n\n')
    f.close()

    return passports


def get_valid_passports(passports):
    valid = 0
    for passport in passports:
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
            valid += 1

    return valid


passports = get_passports_from_input('input')
valid_passports = get_valid_passports(passports)
print(valid_passports)