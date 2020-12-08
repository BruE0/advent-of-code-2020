#!/usr/bin/env python3

"""
    day08.py
    2020
"""


def nop_jmp_change(instructions):
    other = {"jmp": "nop", "nop": "jmp"}
    for i, (instr, n) in enumerate(instructions):
        if instr in ("jmp", "nop"):
            new_instructions = instructions.copy()
            new_instructions[i] = (other, n)
            acc, line_number = accumulator_when_reexecute(new_instructions)
            if line_number == len(instructions):
                return acc


def accumulator_when_reexecute(instructions):
    acc = 0
    lines_seen = set()
    line_number = 0
    while True:
        if line_number in lines_seen or line_number >= len(instructions):
            return acc, line_number
        lines_seen.add(line_number)
        instr, n = instructions[line_number]
        if instr == "jmp":
            line_number += n
        else:
            line_number += 1
            acc += n if instr == "acc" else 0



def main():
    instructions = {}
    with open("day08_input.txt") as f:
        instructions = [
            (instr, int(n)) 
            for line in f
            for instr, n in [line.split()]
    ]


    acc, _ = accumulator_when_reexecute(instructions)
    print(acc) # 1610

    fixed_acc = nop_jmp_change(instructions)
    print(fixed_acc) # 1703

if __name__ == "__main__":
    main()
