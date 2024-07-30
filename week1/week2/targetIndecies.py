def indicesOfTarget(arr: list[int], target: int) -> list[int]:
    indicesArray=[]
  
    
    for index,num in enumerate(arr):
       
       if num==target:
          indicesArray.append(index)
    return indicesArray      
       


print(indicesOfTarget([], 1))
print(indicesOfTarget([5], 5) )
print(indicesOfTarget([5], 1) )
print(indicesOfTarget([1], 1))
print(indicesOfTarget([10,20,30], 1) )
print(indicesOfTarget([10,20,30], 20))
print(indicesOfTarget([30,30,30], 30) )
print(indicesOfTarget([3, 2, 5, 5, 1], 5))