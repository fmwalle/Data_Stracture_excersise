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

def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(toString(reverseBlocks(head,2)))

        

   
