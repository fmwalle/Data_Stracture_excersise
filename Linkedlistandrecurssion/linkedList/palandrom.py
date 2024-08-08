class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def ispalndrom(head):
    if not head:
        return False
    slow=head
    fast=head

    # find the middle
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    # reverse the remining
    prev=None
    while slow:
       temp=slow.next
       slow.next=prev
       prev=slow
       slow=temp
    # check plandrpm
    left,right=head,prev

    while right:
        if left.value!=right.value:
            return False
        left=left.next
        right=right.next
    return True
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
def removeDuplicateFromSorted(head):
    if not head:
        return None
    current=head
 
    while current and current.next :
        if current.value ==current.next.value:
            current.next=current.next.next
        else:    
    
         current=current.next
    return head   
def deleteKNodesAfterMiddle(head,k):
    if not head:
        return None
    # find the middle 
    fast = head
    slow = head
    prev=slow
    while fast and fast.next:
        fast=fast.next.next
        prev=slow
        slow=slow.next
    count=1
    while slow and count<=k:
        count+=1
        prev.next=slow.next
        slow=slow.next
    return head   
# recursive implmention 
def apended(head):
    if not head:
        return 0

    return 1+apended(head.next) 
        



mynode=(Node(1,Node(2,Node(3,Node(4)))))     
print((apended(mynode)))