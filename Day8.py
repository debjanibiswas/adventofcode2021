#!/usr/bin/env python3

def part1():
    data  = open('day8_input.txt').read().splitlines()

    one   = 2  # 2 segments light up to display 1
    four  = 4
    seven = 3
    eight = 7

    output = [i.rpartition('|')[2].strip() for i in data]

    counter = 0
    for i in range(len(output)):
        strings = output[i].split()
        for string in strings:
            length = len(string)
            if length == one or length == four or length == seven or length == eight:
                counter += 1
    
    print(counter)
        
def part2():
    data  = open('day8_input.txt').read().splitlines()
    input = [i.rpartition('|')[0].strip() for i in data]
    output = [i.rpartition('|')[2].strip() for i in data]

    #signals = ['cagedb', 'ab', 'gcdfa','fbcad', 'eafb','cdfbe', 'dab', 'acedgfb']
    summation = 0
    for i in range(len(input)):
        signals = input[i].split()
        display = output[i].split()
        

        one = find1478(signals, 2)
        four = find1478(signals, 4)
        seven = find1478(signals, 3)
        eight = find1478(signals, 7)
        three = findDigit(signals, one, 5)
        six   = find6(signals, one, 6)
        nine = findDigit(signals, four, 6)
        zero = find0(signals, six, nine, 6)
        five = find5(signals, nine, three, 5)
        two = find2(signals, five, three, 5)

        allDigits = [zero, one, two, three, four, five, six, seven, eight, nine]

        number = ''

        for j in display:
            for i in range(len(allDigits)):
                if (containsAll(j, allDigits[i])):
                    number += str(i)
        
        summation += int(number)
    print(summation)
        


# function to check if all characters in set are in str
def containsAll(str, set):
    if(len(str) != len(set)):
        return False

    for c in set:
        if c not in str: 
            return False
    return True

def containsChars(str, set):
    for c in set:
        if c not in str:
            return False
    return True

#little helper functions to find all the digits

# helper to find 1,4,7,8
def find1478(signals, length):    
    for i in range(len(signals)):
        string = signals[i]
        if (len(string) == length):
            return string


# helper to find 3, 5, 9
def findDigit(signals, digit, length):
    for string in signals:
        if (len(string) == length) and containsChars(string, digit):
            return string

# helper to find 6
def find6(signals, one, length):
    for string in signals:
    #    print(string)
        if (len(string) == length and (not containsChars(string,one))):
            return string


# helper to find 0
def find0(signals, six, nine, length):
    for string in signals:
        if ((len(string) == length) and (not string == six) and (not string ==nine)):
            return string

# helper to find 5
def find5(signals, nine, three, length):
    for string in signals:
        if(len(string) == length) and string != three and containsChars(nine,string):
                return string

# helper to find 2
def find2(signals, five, three, length):
    for string in signals:
        if((len(string) == length and string!= five and string!= three)):
            return string


part1()
part2()