def printAllPairs(array: list[int]):
    # Iterate over each element with index i
    for i in range(len(array)):
        # Iterate over each subsequent element with index j
        for j in range(i + 1, len(array)):
            # Print the pair (array[i], array[j])
            print(f"({array[i]}, {array[j]})")


    
print(printAllPairs([1,2,3,4,5]))   


def reverseString(s):
    array=list(s)# [*s]
   
    i=0
    j=len(s)-1
    while(i<j):
     array[i],array[j]=array[j],array[i]
     i+=1
     j-+1
    return "".join(array) 
print(reverseString("Fikir") )  