#!/usr/bin/env python3

"""
    day12_p1.py
    2020
"""


TO_RIGHT = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
TO_LEFT = {v:k for k, v in TO_RIGHT.items()}

def new_direction(direction, command, degrees):
    if command == 'L':
        turning_dict = TO_LEFT
    if command == 'R':
        turning_dict = TO_RIGHT
    for _ in range((degrees%360)//90):
        direction = turning_dict[direction]
    return direction


def update_coordinate(x, y, direction, steps):
    if direction == 'N':
        return x, y + steps
    elif direction == 'S':
        return x, y - steps
    elif direction == 'E':
        return x + steps, y
    else:
        return x - steps, y


def manhattan_distance(x, y):
    return abs(x) + abs(y)



def main():
    with open("day12_input.txt") as f:
        instructions = [(line[0], int(line[1:])) for line in f]

    x = y = 0
    direction = 'E'
    for command, num in instructions:
        if command in 'LR':
            direction = new_direction(direction, command, num)
        elif command in 'F':
            x, y = update_coordinate(x, y, direction, num)
        else:
            x, y = update_coordinate(x, y, command, num)
    
    print(manhattan_distance(x, y)) # 796 (Part One)

if __name__ == "__main__":
    main()
