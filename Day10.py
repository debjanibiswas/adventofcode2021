#!/usr/bin/env python3

def part1():
    data = open('day10_input.txt').readlines()
    
    illegals = []
    closures = {'(':')', '[':']', '{':'}', '<':'>'}
    scores = {')':3, ']':57, '}': 1197, '>':25137}
    
    incompletes = []
    scoreSum = 0
    
    for line in data:
        incompletes.append(line.strip())
        tracker = []
        for i in range(len(line.strip())):
            line = line.strip()
            c = line[i]

            # if it's an opener
            if c in closures:
                tracker.append(closures[c])

            # else if it is a closure
            elif c == tracker[-1]:
                tracker.pop(-1)

            elif c:
                if line in incompletes:
                    incompletes.remove(line)
                scoreSum += scores[c]
                break
            
    print(scoreSum)
    return incompletes

def part2():

    incompletes = part1() # get the list of incompletes from part 1
    closures = {'(':')', '[':']', '{':'}', '<':'>'}
    completes = []

    for line in incompletes:
        tracker = []

        for i in range(len(line.strip())):
            c = line[i]

            # if it's an opener
            if c in closures:
                tracker.append(closures[c])
            
            # else if it is a closure:
            elif c == tracker[-1]:
                tracker.pop(-1)
        tracker.reverse()
        completes.append(''.join(tracker))


    # Now for getting the puzzle output
    scores = []
    for line in completes:
        scores.append(getStringScore(line))

    scores.sort()
    index = int((len(scores)-1)/2)
    print(scores[index])


def getStringScore(line):
    scores = {')':1, ']':2, '}': 3, '>':4}

    totScore = 0
    for c in line:
        totScore = 5*totScore + scores[c]
    return totScore

# part1()
part2()
#print(getStringScore('}}]])})]'))