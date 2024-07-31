class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def findkthfromfirst(head:Node,k:int)->int:
     
     index=1
    
     while head:
        
        if index==k:
          return head.val
        head=head.next
        index+=1
     
     raise("k is un reachable")  



def findKthfromend(head:Node,k:int):
    first=second=head

    for _ in range(k):
        if first ==None:
            raise("the list has a problem")
        first=first.next
    
    while first:
        first=first.next
        second=second.next
    return second.val 

mynode=Node(1,Node(2,Node(3,Node(4,Node(5)))))
#print(findKthfromend(mynode,4)  )


def findthesecondlast(head:Node):
    if head is None or head.next is None:
        raise ValueError("The list must have at least two elements")

  
    counting_len = 0
    first = head
    while first:
        counting_len += 1
        first = first.next

   
   
    
    #current = head
    for _ in range(counting_len-2):
        head = head.next

    return head.val


def findfromlast(head:Node)->int:
    
    if head ==None and head.next==None:
     return None
    
    while head.next.next!=None:
        head=head.next
    return head.val 
mynode=Node(1,Node(2,Node(3,Node(4,Node(5)))))
#print(findfromlast(mynode)  )  

def creatLL(lenthnode:int,values:int)->Node:
    if lenthnode==0:
        return None
    sentintal=Node(00)
    head=sentintal
    for _ in range(lenthnode):
        head.next=Node(values)
        head=head.next
    return sentintal.next
def toString(head:Node):

    if not head:
        return "<empity>"

    parts=[]

    while head:
        parts.append(str(head.val))    
        head=head.next
    return "->".join(parts) 
print(toString(creatLL(5,5)) )

def numPairs(head:Node)->int:
    
    if not head : 
        return 0
    node_dict={}
    while head:
        node_dict[head.val] = node_dict.get(head.val, 0) + 1
        head = head.next
    
    # Count values that occur exactly twice
    count_twice = 0
    for count in node_dict.values():
        if count == 2:
            count_twice += 1
    
    return count_twice

def countElemts(head:Node):
    
    if not head :
        return 0
    countlen=0
    while(head):
        countlen+=1
        head=head.next
        
    return countlen    
    
def findMax(head:Node)->int:
    if not head:
        return None
    maximum=float('-inf')
    while head:
       if head.val>maximum:
           maximum=head.val
       head=head.next
    return maximum   
def printreverseArrayfromLL(head:Node):

    if not head:
        return None
    myreverse=[]
    while head:
        myreverse.append(head.val)
        head=head.next
    i=0
    j=len(myreverse)-1

    while i< j:
        myreverse[i],myreverse[j]=myreverse[j],myreverse[i]
        i+=1
        j-=1
    return myreverse                 
            
mynode = Node(1, Node(2, Node(70, Node(4, Node(50)))))
print(printreverseArrayfromLL(mynode)) 
