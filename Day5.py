#!/usr/bin/env python3

import numpy 

def part1_2(**args):
    data = open('day5_input.txt').read().splitlines()
    #data = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9',
    #        '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
    #data = ['5,5 -> 8,2']
    matrix = []
    for i in data:
        input = i.split(',')
        x1 = int(input[0])
        y2 = int(input[2])

        middle = input[1].split('->')

        y1 = int(middle[0].strip())
        x2 = int(middle[1].strip())
        matrix.append([x1,y1,x2,y2])
        
    maxElement = numpy.amax(matrix) + 1
    #maxElement = 10

    # Now create a matrix with the maxElement
    # board = [[0]*maxElement] * maxElement

    # print(board)

    # for row in board:
    #     print(id(row))

    board = [[0 for _ in range(maxElement)] for _ in range(maxElement)]

    # print('-----')
    # for row in board:
    #     print(id(row))

    pt_list = []

    for points in matrix:
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]

        # check if vertical lines
        pt_range = []

        if(x1 == x2):
            if(y1 > y2):
                pt_range = list(range(y2, y1+1))
            else:
                pt_range = list(range(y1,y2+1))
            for pt in pt_range:
                pt_list.append([pt, x1])
            
            

        # Now check for horizontal lines
        elif(y1 == y2):
            if(x1 > x2):
                pt_range = list(range(x2,x1+1))
            else:
                pt_range = list(range(x1,x2+1))
            for pt in pt_range:
                pt_list.append([y1, pt])

        # now for diagonal lines
        else:
            pt_list.append([y1,x1])
            while(x1 != x2 and y1 != y2):
                if(x1 > x2 and y1 < y2):   #covers examples like (9,7) -> (7,9)
                    x1 = x1 - 1
                    y1 = y1 + 1
                elif(x1 < x2 and y1 < y2): # covers examples like (1,1) -> (3,3)
                    x1 = x1 + 1
                    y1 = y1 + 1
                elif (x1 < x2 and y1 > y2): # covers examples like (5,5) -> (8,2)
                    x1 = x1 +1 
                    y1 = y1 -1 
                else:                       # covers examples like (6,4) -> (2,0)
                     x1 = x1 - 1
                     y1 = y1 - 1
                pt_list.append([y1,x1])
                

    #print(numpy.matrix(pt_list))
    for pts in pt_list:
        row = pts[0]
        col = pts[1]

        board[row][col] += 1

    npArr = numpy.array(board)
    count = numpy.count_nonzero(npArr>1)
    print(count)
    #print(numpy.matrix(board))

part1_2()