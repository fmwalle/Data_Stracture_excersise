class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def removeNodesNotinTraget(head,target):
    if not head:
        return None
    dummy=Node(0)
    dummy.next=head
    prev,current=dummy,head

    while current:
        nxt=current.next

        if current.value!=target:
           prev.next=nxt
        else:
           prev=current
        current=current.next
    return dummy.next
def removeEveryOtherValue(head):
     if not head:
         return None
     current=head
     prev=None
     index=0
     while current:
         if index%2==1:
             if prev:
                 prev.next=current.next
         else:
             prev=current
         current=current.next 
         index+=1
     return head 
def checkPalandrom(head):
    if not head:
        return None
    slow=head
    fast=head
    # we find the middle
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
    # find the palandrom
    left,right=head,prev
    while right:
        if left.value!=right.value:
            return False
        left=left.next
        right=right.next
    return True  
def removeheadandtail(head):
    if not head or not head.next:
        return None
    myhead=head.next
    tail=head
    while tail.next and tail.next.next:
             tail=tail.next
             
    tail.next=None
    return myhead         

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
def sumofTwoLists(head1,head2):
     if not head1 and not head2:
         return None
     if not head1:
         return head2
     if not head2:
         return head1
     sentinetal=Node(0)
     dummy=sentinetal
     while head1 and head2:
         sum=0
         if head1:
             sum+=head1.value
         if head2:
             sum+=head2.value
         dummy.next=Node(sum)
         head1=head1.next
         head2=head2.next
         dummy=dummy.next
     if head1:
         dummy.next=Node(head1.value)
     if head2:
         dummy.next=Node(head2.value)    
     return sentinetal.next                
def interzeroBeforeTheTargetElemnt(head,target):
    if not head:
        return None
    current=head
    dummy=Node(0)
    prev=dummy
    dummy.next=head

    while current:
        if current.value==target:
            newnode=Node(0)
            prev.next=newnode
            newnode.next=current
           
        prev=current    
        current=current.next
    return dummy.next    

            

mynode=(Node(2,Node(2,Node(1,Node(2,Node(4)))))) 
mynode2=(Node(1,Node(2,Node(1,Node(3,Node(4)))))) 

print(print_linked_list(interzeroBeforeTheTargetElemnt(mynode,2)))