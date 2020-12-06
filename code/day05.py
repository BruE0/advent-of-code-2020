#!/usr/bin/env python3

"""
    day05.py
    2020
"""

from itertools import groupby, count


def decode_pass(pas):
    row_i = 0
    row_j = 128
    col_i = 0
    col_j = 8
    for char in pas[:-3]:
        mid = (row_i + row_j) // 2
        if char == 'F':
            row_j = mid
        else:
            row_i = mid
    for char in pas[-3:]:
        mid = (col_i + col_j) // 2
        if char == 'L':
            col_j = mid
        else:
            col_i = mid
    return 8 * row_i + col_i



def main():
    with open("day05_input.txt") as f:
        seat_codes = f.read().splitlines()

    IDs = [decode_pass(code) for code in seat_codes]

    set_IDx = set(IDs)
    left_over_seats = [i for i in range(128*8) if i not in set(IDs)]
    
    c = count()
    lonely_seat = None
    for _, v in groupby(left_over_seats, lambda x: x - next(c)):
        v = list(v)
        if len(v) == 1:
            lonely_seat = v[0]
            break

    print(max(IDs)) # 892 (Part One)
    print(lonely_seat) # 625


if __name__ == "__main__":
    main()
