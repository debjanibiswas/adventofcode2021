#!/usr/bin/env python3

import numpy 
numpy.set_printoptions(threshold=numpy.inf)
def part1():

    data = open('day13_input.txt').readlines()

    coords = []
    rows = []
    cols = []
    lastCoord = 0
    for item in data:
        lastCoord += 1
        # if it is the end of the coordinates and start of the instructions
        if (item == '\n'):
            break
        else:
            item = item.strip()
            (i,j) = item.split(',')
            cols.append(int(i))
            rows.append(int(j))
            coords.append((int(i),int(j)))
    

    maxRow = max(rows) + 1
    maxCol = max(cols) + 1
    print(maxRow)
    print(maxCol)
    
    # for part 1 only need to evaluate the first instruction
    instruction = readInstruction(data[lastCoord]) 
    
    M = numpy.zeros((maxRow,maxCol))

    for i in range(len(cols)):
        row = rows[i]
        col = cols[i]
        M[row][col] = 1
 
    (M1, M2) = foldMatrix(instruction, M)
    finalM = juxtaposeM(M1, M2)

    toSum = finalM == 1
    print('Part 1:' , toSum.sum())

    # Now for part 2
    for i in range(lastCoord+1, len(data)):
        print(instruction)
        instruction = readInstruction(data[i])
        (M1, M2) = foldMatrix(instruction, finalM)
        finalM = juxtaposeM(M1, M2)
  
    print('Part 2:')

    strFinalM = [['.' for i in subList] for subList in finalM]
    for i in range(len(finalM)):
        for j in range(len(finalM[0])):
            if(finalM[i][j] == 0):
                strFinalM[i][j] = ' '
            else:
                strFinalM[i][j] = '#'

    for i in range(len(strFinalM)):
        print(''.join(strFinalM[i]))
    


def readInstruction(instruction):
    parts = instruction.split()[-1].split('=')
    return parts

def foldMatrix(instruction, M):
    print('In Fold Matrix')
    print(M.shape)

    M1 = []
    M2 = []

    # fold vertically
    if(instruction[0] == 'y'):
        M1 = M[0:int(instruction[1]),:]
        M2 = M[int(instruction[1])+1::,:]
        return(M1, numpy.flip(M2,axis=0))

    # fold horizontally
    elif(instruction[0] == 'x'):
        M1 = M[:,0:int(instruction[1])]
        M2 = M[:,int(instruction[1])+1::]
        return(M1, numpy.flip(M2, axis=1))

    
def juxtaposeM(M1, M2):    
    for i in range(len(M2)):
        for j in range(len(M2[0])):
            if(M2[i][j] == 1):
                M1[i][j] = 1
    return M1


part1()