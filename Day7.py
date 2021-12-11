#!/usr/bin/env python3

def part1():
    data = [int(i) for i in open('day7_input.txt').read().split(',')]
    maxPos = max(data) + 1
    result = [0 for _ in range(maxPos)]

    for i in range(len(result)):
        for j in range(len(data)):
            result[i] += abs(data[j] - i)

    print(min(result))

def part2():
    data = [int(i) for i in open('day7_input.txt').read().split(',')]
    maxPos = max(data) + 1
    result = [0 for _ in range(maxPos)]

    for i in range(len(result)):
        for j in range(len(data)):
            result[i] += fuelCost(i, data[j])

    print(min(result))

def fuelCost(startPos, endPos):
    fuelCost = 0
    distance = abs(endPos - startPos) + 1
   
    for i in range(distance):
        fuelCost += i
    return fuelCost

part1()
part2()