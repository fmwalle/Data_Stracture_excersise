class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
def countOdd(head: Node) -> int:
    if not head:
        return 0
    
    count=0
    curr=head
    while curr:
        if curr.value%2!=0:
            count+=1
        curr=curr.next    
    return count
'''
print(countOdd(None) == 0)

# 0
head = Node(0)
print(countOdd(head) == 0)

# 5
head = Node(5)
print(countOdd(head) == 1)

# 6
head = Node(6)
print(countOdd(head) == 0)

# 1 -> 1 -> 1 -> 1
head = Node(1, Node(1, Node(1, Node(1))))
print(countOdd(head) == 4)

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))
print(countOdd(head) == 2)

# 2 -> 2 -> 2 -> 2
head = Node(2, Node(2, Node(2, Node(2))))
print(countOdd(head) == 0)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(countOdd(head) == 3)

# 6 -> 2 -> 100 -> 4 -> 8
head = Node(6, Node(2, Node(100, Node(4, Node(8)))))
print(countOdd(head) == 0)

'''
def strCopies(word: str, sub: str, n: int) -> bool: 
    if not word and not sub:
        return True
    if n==0:
        return True
    if not sub or not str:
        return False
    if len(word)<len(sub):
        return False
    if word[0:len(sub)]==sub:
        return strCopies(word[1:],sub,n-1)
    
    else:
        return strCopies(word[1:],sub,n)
   
print(strCopies("catcowcat", "cat", 2) == True)
print(strCopies("catcowcat", "cow", 2) == False)
print(strCopies("catcowcat", "cow", 1) == True)
print(strCopies("iiijjj", "i", 3) == True)
print(strCopies("iiijjj", "i", 4) == False)
print(strCopies("iiijjj", "ii", 2) == True)
print(strCopies("iiijjj", "ii", 3) == False)
print(strCopies("iiijjj", "x", 3) == False)
print(strCopies("iiijjj", "x", 0) == True)
print(strCopies("iiiiij", "iii", 3) == True)
print(strCopies("iiiiij", "iii", 4) == False)
print(strCopies("ijiiiiij", "iiii", 2) == True)
print(strCopies("ijiiiiij", "iiii", 3) == False)
print(strCopies("dogcatdogcat", "dog", 2) == True)         

