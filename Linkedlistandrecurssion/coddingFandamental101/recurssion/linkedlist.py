class Node:
    def __init__(self,value,next=None):
          self.value=value
          self.next=next
def arrayToLL(array)->Node:
     if not array:
          return None
     dummy=Node(-99)
     head=dummy
    
     for arr in  (array):
          head.next=Node(arr)
          
          head=head.next
     return dummy.next  
def printing(head):
     if not head:
          return None
     curr=head
     while curr:
          print(curr.value,end='->')
          curr=curr.next
     return head     
print(printing(arrayToLL([1,2,3,4])) )    

def stack_Desighn_profit(array)->int:
      max_profit=0
      min_price=float('inf')
    
         
      for curprice in array:
           profit=curprice-min_price

           max_profit=max(profit,max_profit)
           min_price=min(curprice,min_price)
      return max_profit      
           