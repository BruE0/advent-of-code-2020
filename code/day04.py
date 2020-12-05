#!/usr/bin/env python3

"""
    day04.py
    2020
"""

import re

PASSPORT_PATTERN = re.compile(r"(\S+):(\S+)")
REQUIRED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def has_valid_data(passport):
    byr = passport.get('byr', '')
    iyr = passport.get('iyr', '')
    eyr = passport.get('eyr', '')
    hgt = passport.get('hgt', '')
    hcl = passport.get('hcl', '')
    ecl = passport.get('ecl', '')
    pid = passport.get('pid', '')

    valid_ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    hex_digits = '0123456789abcdef'
    return (
        byr.isdigit() and 1920 <= int(byr) <= 2002 and
        iyr.isdigit() and 2010 <= int(iyr) <= 2020 and
        eyr.isdigit() and 2020 <= int(eyr) <= 2030 and
        (   (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193) or
            (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76)
        ) and
        hcl[0:1] == '#' and all(c in hex_digits for c in hcl[1:]) and
        ecl in valid_ecl and
        pid.isdigit() and len(pid) == 9
    )
 

def main(): 
    with open("day04_input.txt") as f:
        passports = f.read().split('\n\n')

    passports_with_required_fields = 0
    passports_with_valid_data = 0
    for string in passports:
        passport = {
            match.group(1) : match.group(2)
            for match in PASSPORT_PATTERN.finditer(string)
        }
        if all(field in passport for field in REQUIRED_FIELDS):
            passports_with_required_fields += 1
            if has_valid_data(passport):
                passports_with_valid_data += 1

    print(passports_with_required_fields) # 210 (Part One)
    print(passports_with_valid_data) # 131 (Part Two)   

if __name__ == "__main__":
    main()
