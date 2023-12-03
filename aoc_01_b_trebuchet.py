#!/usr/bin/python

# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the digits
# are actually spelled out with letters: one, two, three, four, five,
# six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real
# first and last digit on each line. For example:

# two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2
# zoneight234 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14,
# and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

import sys
import re

fname = 'input/01_in.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

sum = 0
with open(fname, 'r') as f:
    for l in f:
        l = l.rstrip('\n')

        # Handle the case eightwothree
        # where the correct interpertation is 8wo3
        # because eight is more left than two

        numlist = []

        while len(l) > 0:
            if re.search(r"^(?:1|one)", l):
                numlist.append(1)
            elif re.search(r"^(?:2|two)", l):
                numlist.append(2)
            elif re.search(r"^(?:3|three)", l):
                numlist.append(3)
            elif re.search(r"^(?:4|four)", l):
                numlist.append(4)
            elif re.search(r"^(?:5|five)", l):
                numlist.append(5)
            elif re.search(r"^(?:6|six)", l):
                numlist.append(6)
            elif re.search(r"^(?:7|seven)", l):
                numlist.append(7)
            elif re.search(r"^(?:8|eight)", l):
                numlist.append(8)
            elif re.search(r"^(?:9|nine)", l):
                numlist.append(9)

            l = l[1:]


        if len(numlist) > 0:
            first = numlist[0]
            last = numlist[-1]

            # print(f'{first}{last} from line {l}')
            sum += (int(first) * 10 + int(last))


print(f'Trebuchet configuration sum: {sum}')

