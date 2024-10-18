class ListNode:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def deleteMiddle(root):
    # find the middle using fast and slow pointer method
    #
    if not root and not root.next:
        return None 
    slow=fast=root
    prev=None

    while fast and fast.next:

        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    return root

def printList(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3)))

print("Original list:")
printList(head)

# Delete the middle node
head = deleteMiddle(head)

print("After deleting the middle node:")
printList(head)        