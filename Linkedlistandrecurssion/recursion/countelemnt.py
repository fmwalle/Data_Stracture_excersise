class Node:

    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def count_elements_recursively(head):

    if not head:
        return 0
    return 1 + count_elements_recursively(head.next)  

head = Node(1, Node(2, Node(3, Node(4))))

print(count_elements_recursively(head))       

def maxrecursive(array):
    if len(array)==1:
        return array[0]
    # using slice number
    return  max(array[0],maxrecursive(array[1:]))
def maxrecurisveArray(array,index=0):
    if len(array)==index+1:
        return array[index]
    
    return max(array[index],maxrecurisveArray(array,index+1))

def maxindexrecursively(array,i=0,max_index=0):
    if i==len(array):
        return max_index
    
    if array[i] > array[max_index]:
        max_index=i
    
    return maxindexrecursively(array,i+1,max_index)
    

print(maxindexrecursively([1,2,3,4,5,7]))  


def sumDigitIterative(n)->int:

    sum=0
    while n>0:
        mod=n%10
        div=n//10
        sum+=mod
        n=div
    return sum
print(sumDigitIterative(66))  

def sumdigitRecursively(n)->int:
    if n<10:
        return n
    return n%10+sumdigitRecursively(n//10)  
print(sumdigitRecursively(66)) 
 

def  countX(word: str) -> int:
  if len(word) <= 0:
    return 0

  if word[0] == 'x':
    return 1 + countX(word[1:])

  return countX(word[1:]) 
print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hiX") == 0) 