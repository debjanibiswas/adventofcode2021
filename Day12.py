#!/usr/bin/env python3

def part1():
    data = open('day12_input.txt').readlines()

    graph = {}

    for path in data:
        points = path.strip().split('-')
        if points[0] not in graph:
            graph[points[0]] = [points[1]]
        else:
            graph[points[0]] += [points[1]]

        if points[1] not in input:
            graph[points[1]] = [points[0]]
        else:
            graph[points[1]] += [points[0]]

    
    print(findPaths('start', graph, ['start']))
    #print(findPaths2('start', input, ['start']))



def findPaths(node, graph, visited):
    
    counter = 0
    if node == 'end':
        #print(f'returning: {visited}')
        return 1
    
    for value in graph[node]:
        if value.islower() and value in visited:
            continue

        counter += findPaths(value, graph, visited + [value])
        
    return counter


part1()