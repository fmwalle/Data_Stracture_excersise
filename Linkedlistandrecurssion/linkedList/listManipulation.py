class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")  
def print_list(head, max_nodes=10):
    nodes = []
    current = head
    count = 0
    while current and count < max_nodes:
        nodes.append(current.value)
        current = current.next
        count += 1
        if current == head:  # Break if we complete a cycle
            break
    print(" -> ".join(map(str, nodes)))      
def createCycle(head):
    if not head:
        return None
    current = head
    while current.next is not None:
        current=current.next
    current.next=head 
    return head
def multiplywithNebour(head):
    if not head:
        return None
    dummy=Node(0)
    prev=dummy
    curr=head
    while curr and curr.next:
        val=curr.value*curr.next.value
        curr.value=val
        curr=curr.next
    val=curr.value*curr.value
    curr.value=val
    return head  
def removeEveryOtherNode(head):
    if not head:
        return None
    curr=head
    while curr and curr.next:
        
        curr.next=curr.next.next
        curr=curr.next
      

    return head  

def reverseRecursively(head):
   if not head:
            return None
   newHead=head
   if head.next:
        newHead=reverseRecursively(head.next)
        head=head.next.next
            
   head.next=None

   return newHead  

mynode=(Node(2,Node(2,Node(1,Node(2)))))
mynode2=(Node(1,Node(2,Node(1,Node(3,Node(4)))))) 

print(print_linked_list(reverseRecursively(mynode)))       
            