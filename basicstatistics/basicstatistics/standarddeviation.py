import math

class standarddeviation():
    numbers = input("Enter the values to analyze: ")
    numlist = numbers.split() #by default is a space

    #numlist is a list of strings, must convert each item to an int
    intlist = []

    for s in numlist :
        intlist.append(int(s))

    #standard deviation
    sum = 0

    for i in intlist :
        sum += (i - average) ** 2

    stddev = math.sqrt(sum / N)
    print("The standard deviation is ", stddev)