def printArray(array: list[int]):
    for number in array:
        print(number)

#printArray([1,2,3,4,5,6,7,8,9,10])  

def printEveryOtherValue(array: list[int]):

    indexing=0
    arrayLenth=len(array)
    for number in array:
        if indexing<arrayLenth:
            print(array[indexing])
            indexing+=2


#printEveryOtherValue([1,2,3,4,5,6,7,8,9,10])  


def printEveryOtherValueSkipFirst(array: list[int]) -> None:

  indexing=1
  arrayLength=len(array)
  for number in array:
    if(indexing<=arrayLength-1):
      print(array[indexing])
      indexing+=2


#printEveryOtherValueSkipFirst([1,2,3,4,5,6,7,8,9,10])

def printEveryKth(array:list[int],k:int):
  arraylenth=len(array)
  start=0
  if(k>=arraylenth):
    return
  for number in array:
    if(start< arraylenth-1):
      print(array[start])
      start+=k

#printEveryKth([1,2,3,4,5,6,7,8,9,10],9)

def printReverse(array: list[int]) -> None:
  arrayLenth=len(array)
  for number in array:
    print(array[arrayLenth-1])
    arrayLenth-=1

#printReverse([1,2,3,4,5,6,7,8,9,10])
def printReverseEveryOtherValue(array: list[int]) -> None:
  arrayLenth=len(array)
  for number in array:
    if arrayLenth>0:
      print(array[arrayLenth-1])
      arrayLenth-=2 
#printReverseEveryOtherValue([1,2,3,4,5,6,7,8,9,10])



def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
  arrayLength=len(array)
  for number in array:
    if arrayLength>0:
      print(array[arrayLength-2])
      arrayLength-=2

#printReverseEveryOtherValueSkipLast([1,2,3,4,5,6,7,8,9,10])

def printReverseEveryKth(array: list[int], k: int) -> None:
  
  arrayLength=len(array)
  if(k>=arrayLength): return
  start=0
  for number in array:
    if arrayLength>0:
      print(array[arrayLength-1])
      arrayLength-=k

printReverseEveryKth([1,2,3,4,5,6,7,8,9,10],1)
      