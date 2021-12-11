#!/usr/bin/env python3

import numpy

def part1():
    data = open('day11_input.txt').read().splitlines()

    matrix = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            matrix.append(int(data[i][j]))
    
    shape = len(data[0])
    matrix = numpy.reshape(matrix, (shape,shape))
    
    
    rows = len(data)
    cols = len(data[0])

    stepCount = 100

    totFlashes = 0
    for step in range(stepCount)
        step += 1
        alreadyFlashed = set()

        matrix = matrix +1  # incremenet all elements of the matrix by 1 in the beginning
        
        Flashed = False
        
        if(10 in matrix):
            Flashed = True

        while(Flashed):
            Flashed = False
            for i in range(rows):
                for j in range(cols):
                    if(matrix[i][j] > 9 and (i,j) not in alreadyFlashed):
                        alreadyFlashed.add((i,j))
                        Flashed = True
                        
                        if (i-1 >= 0): 
                            # degree 1
                            if (j-1 >=0):
                                matrix[i-1][j-1] += 1
                            
                            # degree 2
                            matrix[i-1][j] += 1

                            # degree 3
                            if (j+1 < cols):
                                matrix[i-1][j+1] += 1
                                            
                        # degree 4
                        if (j-1 >= 0):
                            matrix[i][j-1] += 1
                        
                        # degree 5
                        if (j+1 < cols):
                            matrix[i][j+1] += 1
                        
                        if (i+1 < rows):

                            # degree 7
                            matrix[i+1][j] += 1

                            # degree 6
                            if (j-1 >= 0):
                                matrix[i+1][j-1] += 1

                            # degree 8
                            if (j+1 < cols):
                                matrix[i+1][j+1] += 1
        
        # go through the matrix and set flashes to 0
        matrix[matrix > 9] = 0
        currFlashCount = numpy.count_nonzero(matrix==0)
        totFlashes += currFlashCount
        
    print(stepCount)


# part 2 is almost the same as part 1
def part2():
        data = open('day11_input.txt').read().splitlines()

    matrix = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            matrix.append(int(data[i][j]))
    
    shape = len(data[0])
    matrix = numpy.reshape(matrix, (shape,shape))
    
    
    rows = len(data)
    cols = len(data[0])

    stepCount = 0

    totFlashes = 0
    while(True):
        stepCount += 1
        alreadyFlashed = set()

        matrix = matrix +1  # incremenet all elements of the matrix by 1 in the beginning
        
        Flashed = False
        
        if(10 in matrix):
            Flashed = True

        while(Flashed):
            Flashed = False
            for i in range(rows):
                for j in range(cols):
                    if(matrix[i][j] > 9 and (i,j) not in alreadyFlashed):
                        alreadyFlashed.add((i,j))
                        Flashed = True
                        
                        if (i-1 >= 0): 
                            # degree 1
                            if (j-1 >=0):
                                matrix[i-1][j-1] += 1
                            
                            # degree 2
                            matrix[i-1][j] += 1

                            # degree 3
                            if (j+1 < cols):
                                matrix[i-1][j+1] += 1
                                            
                        # degree 4
                        if (j-1 >= 0):
                            matrix[i][j-1] += 1
                        
                        # degree 5
                        if (j+1 < cols):
                            matrix[i][j+1] += 1
                        
                        if (i+1 < rows):

                            # degree 7
                            matrix[i+1][j] += 1

                            # degree 6
                            if (j-1 >= 0):
                                matrix[i+1][j-1] += 1

                            # degree 8
                            if (j+1 < cols):
                                matrix[i+1][j+1] += 1
        
        # go through the matrix and set flashes to 0
        matrix[matrix > 9] = 0
        currFlashCount = numpy.count_nonzero(matrix==0)
        if(currFlashCount == shape * shape):
            break
        totFlashes += currFlashCount
        
    print(stepCount)
                    
part1()
part2()