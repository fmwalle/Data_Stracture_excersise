def array6(array:list[int],index:int)->int:
    if index>=len(array):
        return 0
    if array[index]==6:
        return 1+array6(array,index+1)
   
    return array6(array,index+1)

print(array6([1,2,6,4,6],0))

def traingleBlock(n):
   if n<=0:
       return 0
   
   return n+traingleBlock(n-1)
def bunnyEars(n):
    if n==0:
        return n
    
    return bunnyEars(n-1)
def bunnyEarsTwist(bunnies):
    if bunnies == 0:
      return 0
    if bunnies % 2 == 0:
      return 3 + bunnyEarsTwist(bunnies-1)
    return 2 + bunnyEarsTwist(bunnies-1)

print(bunnyEarsTwist(5))