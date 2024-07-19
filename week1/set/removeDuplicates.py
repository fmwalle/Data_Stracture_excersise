def removeDuplicateFellows(fellows):
  uniqueFellows = set()
  output = []
  for fellow in fellows:
    if fellow not in uniqueFellows:
      uniqueFellows.add(fellow)
      output.append(fellow)
  return output
def removeDuplicateFellows(fellows):
 uniqueFellow=set()
 unique=[]

 for fellow in fellows:
    if fellow not in uniqueFellow:
        unique.append(fellow)
    uniqueFellow.add(fellow)    


def countingUniqueElemnts(array:list[int]):
    if len(array)==0 : return -1
    uniqueElemnts=set()
    counting=0

    for i in array: 
          
        if i not in uniqueElemnts:
            uniqueElemnts.add(i) 
            counting=+1
        else:
            counting=-1
    return counting 

print(countingUniqueElemnts([1,2,2,3,4,3,5,6,]))           
