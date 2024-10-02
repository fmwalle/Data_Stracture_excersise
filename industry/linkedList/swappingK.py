class ListNode:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def swapNodes(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    startCounter=1
    endCounter=0
    counter=0
    current=head
    firstNode=head
    secondNode=head
    while current:
        
        
            
        current=current.next
        counter+=1
    if k>counter:
        return None
    
    endCounter=(counter-k)+1
   
   
    current=head
    counter=1
    while current:
         if startCounter<k:
           startCounter+=1
           firstNode=firstNode.next

         if counter<endCounter: 
             counter+=1
             secondNode=secondNode.next
         current=current.next 
    print(endCounter)      
    firstNode.value,secondNode.value=secondNode.value,firstNode.value
    return head
def toString(head: ListNode) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(9))))))
print(toString(swapNodes(head,2)))
