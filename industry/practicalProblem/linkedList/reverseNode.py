class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
def createArrayInReverse(head):
    if not head:
        return []
    reversedNode=[]
    prev=None
    current=head
    while current is not None:
        nextNode=current.next# reserve our second node pointer
        current.next=prev
        prev=current
        current=nextNode
    current=prev
    while current is not None:
        reversedNode.append(current.value)
        current=current.next
    return reversedNode        
head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))
print(createArrayInReverse(head))
head = Node(1, Node(3, Node(5, Node(2))))
print(createArrayInReverse(head) == [2, 5, 3, 1])

# 4 -> 9 -> 14
head = Node(4, Node(9, Node(14)))
print(createArrayInReverse(head) == [14, 9, 4])

# 5 -> 10 -> 15 -> 20
head = Node(5, Node(10, Node(15, Node(20))))
print(createArrayInReverse(head) == [20, 15, 10, 5])

# 5
head = Node(5)
print(createArrayInReverse(head) == [5])
