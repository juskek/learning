
#* quickSort
# Sorts array values in ascending order 
#! Not working: 
#? Questions: 
# TODO>: 


from random import randint

print("Running examples.py")

#* MISCELLANEOUS FUNCTIONS

def checkSort(array):
    for i in range(0,len(array)-1):
        if array[i] > array[i+1]:
            print('NOT SORTED')
            break
    print('SORTED')

def swapArrEl(array,pos1,pos2):
    array[pos1],array[pos2] = array[pos2],array[pos1]
    return array


#* FIRST TIME ALGORITHM
def quickSort(array):
    
    lenArr = len(array)
    rg = range(0,lenArr)
    
    indices = list(rg)
    
    # base case: 1 element
    if lenArr == 1:
        return array
    
    # base case: 2 elements
    if lenArr == 2:
        # if larger number on left, swap
        if array[0] > array[1]:
            array = swapArrEl(array,0,1)
            
        return array
        
    # recursive case: 3 elements and up
    else:
        # randomly select pivot
        pivotInd = indices[randint(0,lenArr-1)]
        pivotVal = array[pivotInd]
        
        # swap pivot with last element
        # array becomes [a,...,b,pivot]
        array = swapArrEl(array,pivotInd,-1)
        
        # place elements
        # < pivot on left
        # > pivot on right
        
        # find first element from left [a] > pivot
        # -1 for 0 index, -1 to skip pivot
        for i in range(0,lenArr-2):
            fromLeftVal = array[i]
            if fromLeftVal > pivotVal:
                fromLeftInd = i
                break # break for loop
        
        # find first element from right [b] < pivot       
        for i in range(0,lenArr-2):
            # -1 for last element, -1 to skip pivot
            fromRightVal = array[-i-2]  
            if fromRightVal < pivotVal:
                fromRightInd = i
                break 
        
                
        return array

# testArray = [2]
# testArray = [4,2]
testArray = [2,6,5]
# testArray = [2,6,5,3,8,7,1,0]
testArray = quickSort(testArray)
checkSort(testArray)


