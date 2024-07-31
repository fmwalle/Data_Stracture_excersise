class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
def search(listofNode:ListNode,target:int)->bool:

    if not listofNode:
        return False
    

    while listofNode:
        if listofNode.val==target:
            return True
        
        listofNode=listofNode.next

    return False

LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
print(search(None, 1)) # False
print(search(LL1, 2)) # True
print(search(LL1, 4)) # False
print(search(LL1, -1)) # False
print(search(LL1, 10)) # True
print(search(LL1, 11)) # False
