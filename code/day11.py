#!/usr/bin/env python3

"""
    day11.py
    2020
"""


def count_around(grid, y, x):
    return sum(
        0 <= i < len(grid)
        and 0 <= j < len(grid[i])
        and (i, j) != (y, x)
        and grid[i][j] == "#"
        for i in (y - 1, y, y + 1)
        for j in (x - 1, x, x + 1)
    )


def count_sight(grid, y, x):
    total = 0
    for i_add in (-1, 0, 1):
        for j_add in (-1, 0, 1):
            if i_add == j_add == 0:
                continue
            i, j = y + i_add, x + j_add
            while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                element = grid[i][j]
                if element == "#":
                    total += 1
                    break
                if element == "L":
                    break
                i += i_add
                j += j_add
    return total


def modify(grid, allowed, neighbor_function):
    new_grid = []
    for i, row in enumerate(grid):
        new_row = []
        for j, item in enumerate(row):
            if item == "L":
                new_row.append("#" if neighbor_function(grid, i, j) == 0 else "L")
            elif item == "#":
                new_row.append("L" if neighbor_function(grid, i, j) >= allowed else "#")
            else:
                new_row.append(".")
        new_grid.append(new_row)
    return new_grid


def count_seat(grid, seat):
    return sum(item == seat for row in grid for item in row)



def main():
    with open("day11_input.txt") as f:
        start_grid = [list(line.rstrip()) for line in f]

    old_grid = start_grid
    while True:
        new_grid = modify(old_grid, allowed=4, neighbor_function=count_around)
        if all(row1 == row2 for row1, row2 in zip(old_grid, new_grid)):
            break
        old_grid = new_grid

    print(count_seat(new_grid, "#")) # 2183 (Part One)

    old_grid = start_grid
    while True:
        new_grid = modify(old_grid, allowed=5, neighbor_function=count_sight)
        if all(row1 == row2 for row1, row2 in zip(old_grid, new_grid)):
            break
        old_grid = new_grid

    print(count_seat(new_grid, "#"))  # 1990 (Part Two)


if __name__ == "__main__":
    main()
