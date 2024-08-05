class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
# creating a linkedlist        
def creatNode(head):
    if not head:
        return None
    current=head
    while current:
       print(current.value,end="->")
       current=current.next
    print("None")
def insert_at_The_Begining(head,val):
    newNode=Node(val)
    newNode.next=head
    return newNode
def insertAtThe_end(head,value):
    new_Node=Node(value)
    if not head:
        return new_Node
    current=head
    while current.next:
        current=current.next
    current.next=new_Node
    return head 

def deleteNodeByvalue(head,target):
    if not head:
        return None
    if head.value==target:
        return head.next
    current=head
    while current.next:
        if current.next.value==target:
            current.next=current.next.next
            return head
        else:
            current=current.next  
    return head          
def reverse_linkid_List(head):
    if not head:
        return None
    prev=None
    current=head
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node 
    return prev  
def find_kth_element(head, k):
    if not head:
        return None
    if k<0:
        return None
    current=head
    count=0
    while current :
        count+=1
        if count==k:
            return current.value
        current=current.next
        
    return None     
def findTheMiddle(head):
    if not head:
        return None  
    slow=fast=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow.value      

myNode=Node(2,Node(3,Node(4,Node(5,Node(6,Node(7))))))   
print(creatNode(myNode))
print(findTheMiddle(myNode))