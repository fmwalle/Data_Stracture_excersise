class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def swapNode(head):
  if not head:
     return None
  if not head.next:
     return head
  prev=head
  current=head.next

  while current.next:
     temp=prev.value
     prev.value=current.value
     current.value=temp
     prev=current.next
     current=prev.next
  return head
def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)

head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))
print(toString(swapNode(head)))
    
    