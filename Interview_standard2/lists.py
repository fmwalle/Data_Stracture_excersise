class ListNode:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def has_cycle(head:ListNode):
    if not head:
        return True

    slow,fast=head,head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            return True

    return False            

print(has_cycle(None) == False)
print(has_cycle(ListNode(5)) == False)

noCycle1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(has_cycle(noCycle1) == False)

noCycle2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(has_cycle(noCycle2) == False)

# Cyclical
selfCycle = ListNode(2)
selfCycle.next = selfCycle
print(has_cycle(selfCycle))

twoNodeCycle = ListNode(1)
secondNode = ListNode(2, twoNodeCycle)
twoNodeCycle.next = secondNode
print(has_cycle(twoNodeCycle))

sixthNode = ListNode(6)
bigLoop = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, sixthNode)))))
sixthNode.next = bigLoop
print(has_cycle(bigLoop))
