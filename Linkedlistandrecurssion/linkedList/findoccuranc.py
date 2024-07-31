class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
def findOccuerance(node,target)->int:

    if not node:
        return -1
    index=0
    while node:
        if node.val==target:
            return index
        
        node=node.next
        index+=1

    return -1

list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
list2=Node(2)
list3 = Node(-1, Node(-2, Node(-3, Node(-4, Node(-5)))))
list4 = Node(1, Node(2, Node(3, Node(2, Node(1)))))
print(findOccuerance(list1, 9) == -1)
print(findOccuerance(list1, 3) == 2)
print(findOccuerance(list2, 2) == 0)

