#!/usr/bin/env python3

"""
    day07.py
    2020
"""

import re



def generate_dict_from_textfile(filename):
    with open(filename) as f:
        text = f.read()

    bag_pattern = re.compile(r"(.+) bags* contain (.+)")
    bag_count_pattern = re.compile(r"(\d+) (.+) bags*")

    contents = {}
    for bag, inner_string in bag_pattern.findall(text):
        if inner_string == "no other bags.":
            contents[bag] = []
        else:
            inner_bag_strings = inner_string.rstrip('.').split(', ')
            inner_bags = [
                (int(count), name)
                for inner in inner_bag_strings
                for count, name in [bag_count_pattern.match(inner).groups()]
            ]
            contents[bag] = inner_bags
    return contents


def contains_shiny(contents, bag):
    inner_bag_names = [name for count, name in contents[bag]]
    if 'shiny gold' in inner_bag_names:
        return True
    return any(contains_shiny(contents, new_bag) for new_bag in inner_bag_names)


def count_bags_inside(contents, bag):
    total = 0
    for count, name in contents[bag]:
        total += count + count * count_bags_inside(contents, name)
    return total



def main():
    contents = generate_dict_from_textfile('day07_input.txt')

    eventually_shiny = sum(contains_shiny(contents, bag) for bag in contents)
    print(eventually_shiny) # 326 (Part One)

    bags_inside_shiny = count_bags_inside(contents, 'shiny gold')
    print(bags_inside_shiny) # 5635 (Part Two)


if __name__ == "__main__":
    main()
