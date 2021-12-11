#!/usr/bin/env python3


def part1(*args):
    lineCount = 0
    measurementCount = 0
    prevNum = -1
    currNum = -1
    with open('day1_input.txt') as f:
        for line in f:
            lineCount += 1
            if lineCount == 1:
                prevNum = int(line)
            else:
                currNum = int(line)
                if(currNum > prevNum):
                    measurementCount +=1 
                prevNum = currNum   
    print(measurementCount)

def part2(*args):
    lineCount = 0
    windowCount = 0
    prevSum = -1
    currSum = -1
    window =[]
    with open('day1_input.txt') as f:
        for line in f:
            lineCount += 1
            window.append(int(line))
            if lineCount == 3:
                currSum = sum(window)
                window.pop(0)
                if prevSum == -1:
                    prevSum = currSum
                elif currSum > prevSum:
                    windowCount +=1
                prevSum = currSum
                lineCount -= 1

    print(windowCount)

part1()
part2()