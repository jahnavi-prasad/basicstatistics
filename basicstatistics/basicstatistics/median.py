import math

class meadian():
    numbers = input("Enter the values to analyze: ")
    numlist = numbers.split() #by default is a space

    #numlist is a list of strings, must convert each item to an int
    intlist = []

    for s in numlist :
        intlist.append(int(s))

    #median
    intlist.sort()
    index = N // 2
    median = intlist[index]
    print("The median is ", median)