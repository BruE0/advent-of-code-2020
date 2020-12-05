#!/usr/bin/env python3

"""
    day03.py
    2020
"""


with open("day03_input.txt") as f:
    grid = f.read().splitlines()

height = len(grid)
width = len(grid[0])

no_trees_R3_D1 = sum(
    grid[row_idx][(row_idx * 3) % width] == "#" 
    for row_idx in range(1, height)
)

no_trees_R1_D1 = sum(
    grid[row_idx][row_idx % width] == "#" 
    for row_idx in range(1, height)
)

no_trees_R5_D1 = sum(
    grid[row_idx][(row_idx * 5) % width] == "#" 
    for row_idx in range(1, height)
)

no_trees_R7_D1 = sum(
    grid[row_idx][(row_idx * 7) % width] == "#" 
    for row_idx in range(1, height)
)

no_trees_R1_D2 = sum(
    grid[row_idx][(row_idx // 2) % width] == "#" 
    for row_idx in range(2, height, 2)
)

print(no_trees_R3_D1) # 282 (Part One)

print(no_trees_R1_D1 * no_trees_R3_D1 *
      no_trees_R5_D1 * no_trees_R7_D1 *
      no_trees_R1_D2)
# 958815792 (Part Two)
