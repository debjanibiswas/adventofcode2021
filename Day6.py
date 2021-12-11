#!/usr/bin/env python3

import os

def part1(**args):
    numberofDays = 18
    lanternfish = [int(i) for i in open('day6_input.txt').read().split(',')]
    count = len(lanternfish)
    newLanternFish = []

    for i in range(numberofDays):
        for j in range(len(lanternfish)):
            if(lanternfish[j] > 0):
                lanternfish[j] -= 1
            else:
                lanternfish[j] = 6
                lanternfish.append(8)
                count += 1
    print(count)
    print(len(lanternfish))
    

def part2(**args):
    numberofDays = 256
    
    lanternfish = [int(i) for i in open('day6_input.txt').read().split(',')]
    
    fishTracker = [0 for _ in range(9)]
    for index in lanternfish:
        fishTracker[index] += 1
    
    for i in range(numberofDays):
        rotateArray(fishTracker)

    print (sum(fishTracker))

def rotateArray(arr):
    
    arr0 = arr[0]
    arr7 = arr[7]
  
    for i in range(0,(len(arr)-1)):
        arr[i] = arr[i+1]
    arr[-1] = arr0
    arr[6]  = arr0 + arr7

part1()
part2()