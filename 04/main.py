def get_passports_from_input(input_location):
    f = open(input_location, 'r')

    passports = f.read().replace('\n', ' ').split('  ')

    passports_collection = []
    for passport in passports:
        fields = passport.split(' ')

        passport_obj = {}
        for field in fields:
            key, value = field.split(":")
            passport_obj[key] = value

        print(passport_obj)
        passports_collection.append(passport_obj)

    f.close()

    return passports_collection


def part_1_get_valid_passports(passports):
    valid = 0
    for passport in passports:
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
            valid += 1

    return valid


def validate_dates(field, min_date, max_date):
    if field == None:
        return False

    if len(field) < 4:
        return False

    if int(field) < min_date or int(field) > max_date:
        return False

    return True


def validate_height(height):
    print(height)
    unit = height[-2:]

    if unit != 'cm' and unit != 'in':
        print(unit)
        print(123)
        return False

    if unit == 'cm' and (int(height[0:-2]) < 150 or int(height[0:-2]) > 193):
        return False

    if unit == 'in' and (int(height[0:-2]) < 59 or int(height[0:-2]) > 76):
        return False

    return True


def validate_hair_color(color):
    if color[0] != '#':
        return False

    if len(color) != 7:
        return False

    if any(not c.isalnum() for c in color[1:]):
        return False

    return True


def validate_eye_color(color):
    if color == 'amb' or color == 'blu' or color == 'brn' or color == 'gry' or color == 'grn' or color == 'hzl' or color == 'oth':
        return True
    return False


def validate_passport_number(passport_number):
    if len(passport_number) != 9:
        return False

    return passport_number.isdecimal()

# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def part_2_get_valid_passports(passports):
    valid = 0
    for passport in passports:
        # print(passport)
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:

            byr_validate = validate_dates(passport['byr'], 1920, 2002)
            # print(byr_validate)
            yir_validate = validate_dates(passport['iyr'], 2010, 2020)
            # print(yir_validate)
            eyr_validate = validate_dates(passport['eyr'], 2020, 2030)
            # print(eyr_validate)
            hgt_validate = validate_height(passport['hgt'])
            # print(hgt_validate)
            ecl_validate = validate_eye_color(passport['ecl'])
            # print(ecl_validate)
            hcl_validate = validate_hair_color(passport['hcl'])
            # print(hcl_validate)
            pid_validate = validate_passport_number(passport['pid'])
            # print(pid_validate)

            if byr_validate and yir_validate and eyr_validate and hgt_validate and ecl_validate and hcl_validate and pid_validate:
                valid += 1
    return valid


passports = get_passports_from_input('input')

# valid_passports = part_1_get_valid_passports(passports)
# print(f"Valid passports for part 1 = {valid_passports}")

valid_passports = part_2_get_valid_passports(passports)
print(f"Valid passports for part 2 = {valid_passports}")
