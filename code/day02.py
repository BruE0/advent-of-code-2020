#!/usr/bin/env python3

"""
    day02.py
    2020
"""


valid_part_one = valid_part_two = 0

with open("day02_input.txt") as f:
    for line in f:
        policy, password = (x.strip() for x in  line.split(":"))
        char = policy[-1]
        min_, max_ = (int(x) for x in policy[:-1].split("-"))
        if min_ <= password.count(char) <= max_:
            valid_part_one += 1

        if (password[min_-1] == char) ^ (password[max_-1] == char):
            valid_part_two += 1


print(valid_part_one) # 536
print(valid_part_two) # 558
