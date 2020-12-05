#!/usr/bin/env python3

"""
    day01.py
    2020
"""


with open("day01_input.txt") as f:
    numbers = [int(n) for n in f]

numberset = set(numbers)

for num in numbers:
    if 2020 - num in numberset:
        part_one_solution = (2020 - num) * num
        break


for i, n1 in enumerate(numbers):
    for n2 in numbers[i:]:
        if 2020 - n1 - n2 in numberset:
            part_two_solution = (2020 - n1 - n2) * n1 * n2
            break

print(part_one_solution) # 1016964
print(part_two_solution) # 182588480
