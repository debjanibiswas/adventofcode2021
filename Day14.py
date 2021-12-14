#!/usr/bin/env python3

def part1():
    data = open('day14_input.txt').readlines()
    template = data[0]
    rules = {}

    for i in range(2,len(data)):
        parts = data[i].strip().split('->')
        rules[parts[0].strip()] = parts[1].strip()

    stepCount = 10
    start_polymer = data[0].strip()

    for i in range(stepCount):
        new_polymer = step(start_polymer, rules)
        start_polymer = new_polymer
    
    print('Part 1:')
    (maxChar, minChar) = countOccurence(start_polymer)

    print(maxChar-minChar)
    

    #print(rules)

def step(polymer, rules):
    newPolymer = ''
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        rule = rules[pair]
        newPolymer += pair[0] + rule
    
    return newPolymer + polymer[-1]
        

def countOccurence(polymer):
    freq = {}
    for c in polymer:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    maxChar = max(freq, key=freq.get)
    minChar = min(freq, key=freq.get)
    return (freq[maxChar], freq[minChar])


part1()