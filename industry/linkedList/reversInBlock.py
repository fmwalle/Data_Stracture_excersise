class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next



def reverseBlocks(head: Node, k: int) -> Node:
    
    if not head or k<=1:
        return head
    count=1
    dummy=Node(0)
    dummy.next=head
    prev=dummy
    current=head

    while current.next:
        while count<k:
            firstNode=current
            secondNode=current.next

            prev.next=secondNode
            firstNode.next=secondNode.next
            secondNode.next=prev

            current=firstNode.next
            prev=secondNode
            count+=1
        current=current.next
    return dummy.next
def reverseKGroupInLL(head,k):
    if not head or k<=1:
        return head
    count=1
    dummy=Node(0)
    prev=None
    createdNode=dummy
    current=head

    while current.next:
        createdNode.next=current
        createdNode=createdNode.next
        if count==k:
           while createdNode.next:
            nextNode=createdNode.next 
            createdNode.next=prev
            prev=createdNode
            createdNode=nextNode
            count=1
        count+=1   
        current=current.next 
    return prev    

def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(toString(reverseKGroupInLL(head,2)))

        

   
