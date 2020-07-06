import math

class mean():
    numbers = input("Enter the values to analyze: ")
    numlist = numbers.split() #by default is a space

    #numlist is a list of strings, must convert each item to an int
    intlist = []

    for s in numlist :
        intlist.append(int(s))

    #mean
    sum = 0

    for i in intlist :
        sum += i

    N = len(intlist)
    average = sum / N
    print("The Mean value is", average)