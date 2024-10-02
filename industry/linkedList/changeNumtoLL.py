class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

def changNumtoLL(num):

    dummy=Node(0)
    current=dummy

    while num>0:

        modu=num%10
        num=num//10
        current.next=Node(modu)
        current=current.next
    prev=None
    current=dummy.next
    while current:
      nextNode=current.next
      current.next=prev
      prev=current
      current=nextNode


    return prev

def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)

def swapingTwoadgesntNode(head):
   if not head or head.next:
      return None
   current=head

   while current and current.next:
      firstNode=current
      secondNode=current.next

      firstNode.value,secondNode.value=secondNode.value,firstNode.value
      current=secondNode.next
   return head   
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(toString(changNumtoLL(123)))


