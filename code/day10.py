#!/usr/bin/env python3

"""
    day10.py
    2020
"""


from collections import Counter


def combinations(adapters):
    acc = {0: 1}
    for adapter in adapters:
        acc[adapter] = acc.get(adapter-3, 0) + acc.get(adapter-2, 0) + acc.get(adapter-1, 0)
    return acc[adapters[-1]]


def main():
    with open("day10_input.txt") as f:
        adapters = [0] + sorted(int(line) for line in f)

    adapters.append(max(adapters) + 3)
    differences = Counter(b - a for a, b in zip(adapters , adapters[1:]))

    print(differences[1] * differences[3]) # 1920 (Part One)

    print(combinations(adapters[1:])) # 1511207993344 (Part Two)

if __name__ == "__main__":
    main()
