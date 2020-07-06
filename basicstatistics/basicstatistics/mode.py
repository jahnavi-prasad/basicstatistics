import math

class mode():
    numbers = input("Enter the values to analyze: ")
    numlist = numbers.split() #by default is a space

    #numlist is a list of strings, must convert each item to an int
    intlist = []

    for s in numlist :
        intlist.append(int(s))
    
    #mode
    index = 0
    maxmode = 0
    modelist = []

    while index < N:
        c = intlist.count( intlist[index] )
        if c > maxmode :
            maxmode = c
            modelist = [ intlist[index] ]
        elif c == maxmode :
            modelist.append( intlist[index] )

        index += c

    print("The mode values that occured" , maxmode, "times are: ", modelist)