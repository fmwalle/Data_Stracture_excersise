class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def printNode(head):
    if not head:
        return None
    current=head
    while current:
        print(current.value,end="->")
        current=current.next
      
def reverseLinked(head)->Node:
    stack=[]
    if not head:
        return None
    current=head
    while current:
        stack.append(current.value)
        current=current.next
    current=head    
    while stack:
        current.value=stack.pop()
        current=current.next  
    return head
def rotatingStringby2(mystr,rotateposition)->str:
    if not mystr:
        return ""
    queue=[]
    answer=""
    start=len(mystr)-rotateposition
    print(len(mystr))
    for i in range(start+1,len(mystr)):
        
        queue.append(mystr[i])
    for i in range(0, start):
        queue.append(mystr[i])
    while queue:
        answer += queue.pop(0)

    return answer
    
print(rotatingStringby2("abcde",2))
mynode=Node(2,Node(3,Node(4)))   
print(printNode(reverseLinked(mynode)))   