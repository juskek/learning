# Self Describing Numbers
# Programming challenge description:
# A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.
# Input:
# Your program should read lines of text from standard input. Each line contains a single positive integer, N.
# Output:
# For each input N, print 1 to standard output if N is a self-describing number. Otherwise, print 0.

# For the curious, here''s how 2020 is a self-describing number: Position 0 has value 2 and there are two 0s in the number. Position 1 has value 0 because there are no 1's in the number. Position 2 has value 2 and there are two 2's. And the position 3 has value 0 and there are zero 3's.


# import pandas as pd
# import numpy as np

print("IMPORTS SUCCESSFUL")

def selfDescNo(N):
    # this function should check if
    # value of index is equal to
    # number of occurences of that index
    selfDescribing = True
    indexValues = {}

    
    valueOccurences = {}
    # initialise with zeros
    for index in range(0,len(N)):
        valueOccurences[str(index)] = 0
    
    # dictionary?
    # brute force: 
    # 1. pass through array,
    # 1a. store index value
    # 1b. count occurences of index
    # 2. then compare both dictionaries by
    # 2a. checking non zero 
    
    # 1.
    for index in range(0,len(N)):
        indexValue = N[index]
        
        # 1a.
        indexValues[str(index)] = int(indexValue)
        
        # 1b.
        
        valueOccurences[indexValue] += 1

        
    for key in indexValues:
        if indexValues[key] != valueOccurences[key]:
            selfDescribing = False
            break
        
    
    try:
        pass
    except:
        pass
    finally:
        pass
    
    if selfDescribing == True:
        print("1")
    elif selfDescribing == False:
        print("0")
    else:
        print("Exception: selfDescribing")
        
        
test = '2020'
selfDescNo(test)