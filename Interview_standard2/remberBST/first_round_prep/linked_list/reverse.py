class Node:
    def __init__(self,value,next=None) :
         self.value=value
         self.next=next


def reverse_linkd(head):
     if not head:
          return None
     
     curr=head

     prev=None

     while curr:
          temp=curr.next
          curr.next=prev
          prev=curr
          curr=temp
     return prev      

def mergeTwoLists(list1, list2):
     # sorting and merge two lists
    if not list1 and not list2:
          return None
    if not list1 and list2:
         return list2
    if not list2 and list1:
         return list1
    dummy=Node(0)
    curr=dummy

    while list1 and list2:
        if list1.value<=list2.value:
              curr.next=Node(list1.value)
              curr.next.next=Node(list2.value)
              list1=list1.next
        else:
           curr.next=Node(list2.value)
           curr.next.next=Node(list1.value) 
           list2=list2.next 

        curr=curr.next
        list1=list1.next
       

    if list1:
         curr.next=list1
         curr=curr.next

    if list2:
       curr.next=list2
    return dummy.next 


def addTwoNumbers(l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1

        list1=[]
        list2=[]

        while l1:
            list1.append(l1.val)
            l1=l1.next 
        while l2:
            list2.append(l2.val)
            l2=l2.next
        list1=reversed(list1)
        list2=reversed(list2)

        newArray=[]
        left=0
        if len(list1)==len(list2):
            for val1,val2 in zip(list1,list2):
                sum=val1+val2
                if left==0:
                 
                  if sum<10:
                   
                    newArray.append(sum)
                  elif sum>=10:
                    val=sum%10
                    newArray.append(val)
                    left=sum//10
                else:
                    sum=sum+left
                    if sum<10:
                   
                       newArray.append(sum)
                    elif sum>=10:
                      val=sum%10
                      newArray.append(val)
                      left=sum//10  
                        

              
