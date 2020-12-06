#!/usr/bin/env python3

"""
    day06.py
    2020
"""

from functools import reduce
from string import ascii_lowercase


def main():
    with open("day06_input.txt") as f:
        all_answers = [
            group.splitlines()
            for group in f.read().split("\n\n")
        ]

    total_count = 0
    for group in all_answers:
        total_count += len(set(''.join(group)))

    print(total_count) # 7120 (Part One)

    actual_total_count = 0
    for group in all_answers:
        actual_total_count += len(
            reduce(lambda x, y: set(x) & set(y), group, ascii_lowercase)
        )

    print(actual_total_count) # 3570 (Part Two)


if __name__ == "__main__":
    main()
