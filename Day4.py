#!/usr/bin/env python3

import numpy
from copy import copy, deepcopy


def part1_2(**args):
    allBoards = []
    input = []
    boardCols = []
    matrix = []
    winnerSum = 0
    allBoardsLoser = []
    loserBingoNum = 0

    data = open('day4_input.txt').read().splitlines()
    input = [int(i) for i in data[0].split(',')]


    for i in range(1, len(data), 6):
        lines = data[i+1:i+6]
        matrix=[]
        for j in range(0,len(lines)):
            array = lines[j].split()
            matrix.append(array)
        allBoards.append(matrix)    
    
    for i in range(len(allBoards)):
            allBoards[i] = [[int(j) for j in i] for i in allBoards[i]]

    allBoardsLoser = allBoards

    # Part 1 - find out which one will be the 1st winner
    for bingoNum in input:
        for i in range(len(allBoards)):
            allBoards[i] = setBoard(allBoards[i], bingoNum)  # punch the numbers in the board 
            if(isWinner(allBoards[i])):  #check if they are a winner
                winnerSum = sumBoard(allBoards[i])
                allBoards.remove(allBoards[i])
                print(winnerSum * bingoNum) 
                break
        else:
            continue
        break


    # Part 2 - find out which one will be the last winnder
    lastBingoNum = 0
    totBingoBoards = len(allBoards)
    boardCounter = 0
    for bingoNum in input:      
        for i in range(len(allBoards)):
            allBoards[i] = setBoard(allBoards[i] , bingoNum)
            if numpy.sum(allBoards[i])==0:
                continue
            if(isWinner(allBoards[i])):
                if(totBingoBoards == 1):
                    print(allBoards[i])
                    print(sumBoard(allBoards[i])* bingoNum)
                    exit()
                allBoards[i] = setZeros(allBoards[i])
                totBingoBoards -= 1
                   
                

def setZeros(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0
    return board
                
      

def setBoard(board, input):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == input:
                board[i][j] = -1
                return board
    return board

                
def isWinner(board):
    boardRowSum = numpy.sum(board, axis=1)  #sum board rows
    boardColSum = numpy.sum(board, axis=0)  #sum board columns
    if(-5 in boardRowSum or -5 in boardColSum or numpy.sum(board)==0):
        return True
    else:
        return False



def sumBoard(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != -1:
                sum += board[i][j]
    return sum
    


part1_2()