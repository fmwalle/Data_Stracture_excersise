class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

def everyKthNode(node: Node, target: int) -> Node:
    if not node or target<=0:
        return None
    count=1
    current=node
    dummy=Node()
    newNode=dummy
    while current != None:
       
        if count==target:
            newNode.next=Node(current.value)
            newNode=newNode.next
            count=0
         
        current=current.next
        count+=1   
    return dummy.next 
def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next
  return " -> ".join(parts)
               
head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))
print(toString(everyKthNode(head, 3)) == "6 -> 9")
print(toString(everyKthNode(head, 1)) == "1 -> 3 -> 6 -> 2 -> 8 -> 9")
print(toString(everyKthNode(head, 5)) == "8")
print(toString(everyKthNode(head, 6)) == "9")
print(toString(everyKthNode(head, 7)) == "<empty>")