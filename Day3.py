#!/usr/bin/env python3 

import math

def part1(**args):
    lineCount = 0
    numDict = []
    totDigits = 0
   
    with open('day3_input.txt') as f:
        for line in f:
            digits = list(line.strip())
    
            i=0
            lineCount += 1
            if(lineCount == 1):
                numDict = [0] * len(digits)
            for digit in digits:
                if(digit =='1'):
                    numDict[i] += 1
                i += 1
            
    totDigits = i
    majority = int(lineCount / 2)
    gamma = ""
    epsilon = ""
    for i in numDict:
        if (i > majority):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print(int(gamma,2) * int(epsilon,2))
    return int(totDigits)

def part2(**args):
    o2 = []
    co2  = []
    
    totDigits = part1()

    with open('day3_input.txt') as f:
        co2 = f.readlines()
    
    # iterate through all the digits
    o2 = co2
    for i in range(0,totDigits):
        maxBool = 0
        minBool = 0
        if(len(o2) > 1):
            maxBool = maxUtils(o2, i) # produce the max boolean in that list
            o2 = selectList(o2, maxBool, i)
        
        if(len(co2) > 1):
            minBool = 1 - int(maxUtils(co2, i))
            co2 = selectList(co2, minBool, i)
    print(int(o2[0],2) * int(co2[0],2))
    

# take a list and produce whether or not 1 or 0 is the max 
def maxUtils(inputList, index):
    numDict = [0] * len(inputList[0])  # dict as long as the number of digits
    majority = int(math.ceil(len(inputList)/2))

    for item in inputList:
        i=0
        digits = list(item.strip()) # get rid of any spaces or newlines
        for digit in digits:
            if(digit =='1'):
                numDict[i] += 1
            i += 1
    if (numDict[index] >= majority):
        return 1
    else:
        return 0




# helper to select specific items on a list 
# maxVal is the chosen boolean value
def selectList(inputList, maxVal, index):
    returnList = []
    for item in inputList:

        if(int(item[index]) == maxVal):
            returnList.append(item.strip())
    return returnList

part1()
part2()