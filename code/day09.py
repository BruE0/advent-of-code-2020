#!/usr/bin/env python3

"""
    day09.py
    2020
"""


def subarray_sum(target, numbers):
    total = 0
    cumsum = {-1: 0}
    for idx, num in enumerate(numbers):
        total += num
        if total - target in cumsum:
            return cumsum[total - target], idx + 1
        cumsum[total] = idx + 1


def find_sum(target, full_list, start_index, end_index):
    set_nums = set()
    for number in full_list[start_index: end_index]:
        if target - number in set_nums:
            return number, target - number
        set_nums.add(number)



def main():
    with open("day09_input.txt") as f:
        code = [int(n) for n in f]

    for i, target in enumerate(code[25:], 25):
        sum_ = find_sum(target, code, i-25, i)
        if sum_ is None:
            failed_number = target
            break

    print(failed_number) # 27911108 (Part One)

    start_idx, end_idx = subarray_sum(failed_number, code)
    contiguous_numbers = code[start_idx: end_idx]
    smallest = min(contiguous_numbers)
    biggest = max(contiguous_numbers)

    print(smallest + biggest) # 4023754 (Part Two)


if __name__ == "__main__":
    main()
