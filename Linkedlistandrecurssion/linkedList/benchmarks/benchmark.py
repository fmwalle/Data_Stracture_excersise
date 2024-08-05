class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def deleteDuplicate(head) :
    if not head:
        return None
    current=head
    while current and current.next:
        if current.value==current.next.value:
            current.next=current.next.next
        else:    
         current=current.next
    return head
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def returnMiddle(head):
    if not head:
        return None
    fast=slow=head

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow.value  
def replaceHeadValue(head):
    if not head:
        return None
    temp=head.value
    current=head
    while current.next:
        current=current.next
        head.value=current.value
       
        
    current.value=temp    
    return head      



head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
updated_head = replaceHeadValue(head)
print(linked_list_to_list(updated_head))
            
