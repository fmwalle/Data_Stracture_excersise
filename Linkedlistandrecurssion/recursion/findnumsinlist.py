class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def exist_in_list(head:Node,target:int)->bool:
    if not head:
        return None
    
    if head.value==target:
        return True
    exist_in_list(head.next,target)
def countOccurance(head:Node,target)->int:
    if not head:
        return -1
    count=1 if head.value==target else 0

    return count+countOccurance(head.next,target)

def find_Min(array:list[int],cuentMin=float('inf'),index=0)->int:

    if index < len(array):

        return find_Min(array,min(cuentMin,array[index]),index+1)
    return cuentMin

#print(find_Min([9,3,2,0,40,1]))

def find_mean(array,n=0,sum=0):
    if not array:
        return 0 if n==0 else sum/n
    
    return find_mean(array[1:],n+1,sum+array[0])
print(find_mean([1,2,3,4,5,6]))  

def replace_negatives(head):
    if not head:
        return
    
    if head.value < 0:
        head.value = 0
    
    replace_negatives(head.next)
myNode = Node(-1, Node(5, Node(-3, Node(2))))


print(replace_negatives(myNode)  )

            