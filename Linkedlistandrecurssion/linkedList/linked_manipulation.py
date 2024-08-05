class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def removedNthelemntfromEnd(head,n):

    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy
    

    for _ in range(n + 1):
        fast = fast.next
    
 
    while fast:
        fast = fast.next
        slow = slow.next
    

    slow.next = slow.next.next
    
    return dummy.next

def printNode(head):
   while head:
      print(head.value,end="->")
      head=head.next
def after0(head):
    if not head:
        return None
    current=head
    while current:
        newNode=Node(0)
        curnext=current.next
        current.next=newNode
        newNode.next=curnext
        current=newNode.next
    return head 
def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.value))
    head = head.next

  return " -> ".join(parts)

def createPalindromeLL(arr: list[int]) -> Node:

    if not arr:
        return None
    dummy=Node(0)
    current=dummy
    for i in arr:
        current.next=Node(i)
        current=current.next
    for i in range(len(arr)-2,-1,-1):
        current.next=Node(arr[i])
        current=current.next
    return dummy.next
#print(toString(createPalindromeLL([20,15,10,5])) )       
def isPalandrome(head):
    if not head:
        return False
    prev=None
    current=head
    array=[]
    while current:
        next_node=current.next
        current.next=prev
        prev=current
       
        current=next_node
    

    return prev 
def findMissing(head):
    if not head:
        return -1
    current=head
    while  current and current.next:
        val=current.value+1
        if current.next.value != val:
            return val
        else:
            current=current.next
    return current.value+1           

 

mynode=Node(1,Node(2,Node(4,Node(5))))
print(findMissing(mynode))
