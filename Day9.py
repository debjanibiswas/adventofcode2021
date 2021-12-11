#!/usr/bin/env python3
import heapq
import numpy

def part1():
    data = open('day9_input.txt').read().splitlines()
    
    lowest = []
    indices = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            c = data[i][j]

            # check if it is the top left corner
            if i == 0 and j == 0:
                right = data[i][j+1]
                bottom = data[i+1][j]
                if (c < right and c < bottom): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))


            # check if it is the top right corner
            elif i==0 and j==len(data[i])-1:
                left = data[i][j-1]
                bottom = data[i+1][j]
                if(c < left and c < bottom): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))
            
            # check if it is the bottom left corner
            elif i== len(data)-1 and j==0:
                top = data[i-1][j]
                right = data[i][j+1]
                if (c < top and c < right): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))
            
            # check if it is the bottom right corner
            elif i == len(data)-1 and j==len(data[i])-1:
                top = data[i-1][j]
                left = data[i][j-1]
                if (c < top and c < left): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))
            
            # check if it is the top line but not the corners
            elif i == 0 and j >0 and j < len(data[i])-2:
                right = data[i][j+1]
                left = data[i][j-1]
                bottom = data[i+1][j]

                if (c < right and c < left and c < bottom): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))
            
            # check if it is the bottom line but not the corners
            elif i == len(data)-1 and j > 0 and j < len(data[i])-1:
                right = data[i][j+1]
                left = data[i][j-1]
                top = data[i-1][j]
                if (c < right and c < left and c < top): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))

            # check the left edge
            elif i > 0 and i < len(data)-1 and j == 0:
                right = data[i][j+1]
                bottom = data[i+1][j]
                top = data[i-1][j]
                if (c < right and c < bottom and c < top): 
                    lowest.append(int(c)+1)
                    indices.append((i,j))
            
            # check the right edge
            elif i > 0 and i < len(data)-1 and j == len(data[i])-1:
                left = data[i][j-1]
                bottom = data[i+1][j]
                top = data[i-1][j]
                if c < left and c < bottom and c < top: 
                    lowest.append(int(c)+1)
                    indices.append((i,j))

            # otherwise it is in the middle
            else:
                left = data[i][j-1]
                right = data[i][j+1]
                bottom = data[i+1][j]
                top = data[i-1][j]
                if c < left and c < right and c < bottom and c < top: 
                    lowest.append(int(c)+1)
                    indices.append((i,j))

    print(sum(lowest))
    return indices
            # check if it is the bottom right corner

def part2():
    data = open('day9_input.txt').read().splitlines()
    
    allIndices = part1()
    basinSize = []

    for index in allIndices:
        basin = findBasin(index, data)
        newBasin = optimizeBasin(basin, data)
        basinSize.append(len(newBasin))
    
    largest = heapq.nlargest(3, basinSize)
    print(numpy.prod(heapq.nlargest(3,basinSize)))


def findBasin(index, data):
    row,col = index
    basin = set([index])


    # Traverse down
    for i in range(row, len(data)):
       
        if(int(data[i][col]) == 9) or (i+1 < len(data) and int(data[i+1][col]) < int(data[i][col])):      
            break
        else:
            if(i+1 < len(data) and int(data[i+1][col]) > int(data[i][col])):   
                basin = basin.union(findBasin((i+1, col), data))    

    # Traverse right
    for j in range(col, len(data[row])):
        # print("Going Right")
        # print((row,j))
        # print(data[row][j])
        # print(data[row][j+1])
        if(int(data[row][j]) == 9) or (j+1 < len(data[row]) and int(data[row][j+1]) < int(data[row][j])):
            break
        else:
            if(j+1 < len(data[row]) and int(data[row][j+1]) > int(data[row][j])):
                basin = basin.union(findBasin((row, j+1), data))    

    # Traverse left
    for j in reversed(range(col+1)): 
         
        if(int(data[row][j]) == 9 or (j>0 and int(data[row][j-1]) < int(data[row][j]))):        
            break
        else:
            if (j>0 and int(data[row][j-1]) > int(data[row][j])):
                basin = basin.union(findBasin((row, j-1), data))   

    # Traverse top
    for i in reversed(range(row+1)):
        
        if(int(data[i][col]) == 9 or (i>0 and int(data[i-1][col]) < int(data[i][col]))):
            break
        else:
            if (i>0 and int(data[i-1][col]) > int(data[i][col])):
                basin = basin.union(findBasin((i-1, col), data))   
    return basin

def optimizeBasin(basin, data):
    newBasin = []
    for (i,j) in basin:
        if int(data[i][j]) != 9:
            newBasin.append((i,j))
    return newBasin

part2()