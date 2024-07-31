def factorial(n)->int:
    if n<0:
        return -1
    elif n<2:
        return 1
    factor=1
    for i in range(1,n+1):
       factor*=i
    return factor

def recursively(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else :
        return n*recursively(n-1)
print(recursively(5))  

def recursiveMax(array,curMax=float('-inf'),i=0)->int:
      if i <len(array):
          return recursiveMax(array, max(curMax,array[i]),i+1)
      return curMax
print(recursiveMax([1,2,3,4,5,90]))

   

    