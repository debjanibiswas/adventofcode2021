#!/usr/bin/env python3

def part1(**args):
    with open ('day2_input.txt') as f:
        horizontal = 0
        depth = 0
        for line in f:
            x = line.split()
            direction = x[0]
            position = int(x[1])
            if(direction == 'forward'):
                horizontal += position
            elif (direction == 'down'):
                depth += position
            elif (direction == 'up'):
                depth -= position

        print(horizontal*depth)
      

def part2(**args):
    with open('day2_input.txt') as f:
        horizontal = 0
        aim = 0
        depth = 0
        for line in f:
            x = line.split()
            direction = x[0]
            position = int(x[1])
            if(direction == 'forward'):
                horizontal += position
                depth += position * aim
            elif (direction == 'down'):
                aim += position
            elif (direction == 'up'):
                aim -= position

    print(horizontal * depth)

part1()
part2()
        