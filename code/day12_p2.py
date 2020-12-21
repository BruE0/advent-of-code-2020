#!/usr/bin/env python3

"""
    day12_p2.py
    2020
"""


def new_waypoint(waypoint, command, number):
    x, y = waypoint
    if command in 'LR':
        clockwise = command == 'L'
        for _ in range((number%360)//90):
            if clockwise:
                x, y = -y, x
            else:
                x, y = y, -x
    else:
        if command == 'N':
            y += number
        elif command == 'S':
            y -= number
        elif command == 'E':
            x += number
        else:
            x -= number
    return x, y


def manhattan_distance(x, y):
    return abs(x) + abs(y)



def main():
    with open("day12_input.txt") as f:
        instructions = [(line[0], int(line[1:])) for line in f]

    waypoint = (10, 1)
    x = y = 0
    for command, num in instructions:
        if command in 'NSWELR':
            waypoint = new_waypoint(waypoint, command, num)
        else:
            x += waypoint[0] * num
            y += waypoint[1] * num

    print(manhattan_distance(x, y)) # 39446 (Part Two)


if __name__ == "__main__":
    main()
