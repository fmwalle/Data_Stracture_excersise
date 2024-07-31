class Node:
    def __init__(self, val, next = None):
        self.val=val
        self.next=next


def arrayToLL(array:list[int])->Node:

    sentinetal=Node(-999)
    cur=sentinetal

    for i in range(0,len(array)):
        cur.next=Node(array[i])
        cur=cur.next
    return sentinetal.next

def toString(head:Node):

    if not head:
        return "<empity>"

    parts=[]

    while head:
        parts.append(str(head.val))    
        head=head.next
    return "->".join(parts)    

print(toString(arrayToLL([])) )
print(toString(arrayToLL([1])) )
print(toString(arrayToLL([1,2])) )
