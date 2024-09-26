class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
def reverseseOrder(head,k):
    if not head:
        return None

    lesskDummy=Node(0)
    gretaerKDummy=Node(0)
    lessk=lesskDummy
    greaterk=gretaerKDummy
    current=head
   
    while current:
        if current.value<k:
            lessk.next=current
            lessk=lessk.next
           
        elif current.value>=k:
            greaterk.next=current
            greaterk=greaterk.next
            
        current=current.next
    greaterk.next=None
    lessk.next=gretaerKDummy.next
    return lesskDummy.next
def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)                  

head = Node(3, Node(6, Node(4, Node(7,Node(2,Node(5,Node(1)))))))
print(toString(reverseseOrder(head,4)))                   