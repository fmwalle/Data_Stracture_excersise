from collections import deque
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left

def maxSumofeveryOtherChild(root):
    if not root:
        return 0
    curr=root
    sum=0
    while curr.left and curr.right:
        sum+=curr.value
        sum=max(curr.value,sum)
        curr=curr.left.left
        curr=curr.right.right
    return sum 
def addEvenValuedParent(root):
    if not root:
        return 0
    sum=0
    def helperAdd(node):
        if not node:
            return None
        nonlocal sum
        if node.value%2==0:
            if node.left:
                sum+=node.left.value
            if node.right:
                sum+=node.right.value
        helperAdd(node.left)
        helperAdd(node.right)
    helperAdd(root)
    return sum  
def treeFlip(root):
    if not root:
        return None
    temp=root.left
    root.left=root.right
    root.right=temp
    treeFlip(root.right)
    treeFlip(root.left )
    return root
def findElemntsinBfs(root,target):
    if not root:
        return False
    queue=deque([root])
    while queue:
        currentNode=queue.popleft()
        if currentNode:
            if currentNode.value==target:
                return True
        else:
            continue
        queue.append(currentNode.left) 
        queue.append(currentNode.right) 
    return False    
#print(addEvenValuedParent(None) == 0)

#     6
#  7     8
# 2 7   1 3
root = Node(6,
  Node(7,
     Node(2),
     Node(7)
  ),
  Node(8,
      Node(1),
      Node(3)
  )
)
root = Node(5)
treeFlip(root)
print(root.value == 5)
root = Node(5,
  Node(10),
  Node(5))
treeFlip(root)
print(
  root.value == 5,
  root.left.value == 5,
  root.right.value == 10,
  root.left.left == None, # verify leaf node
  root.left.right == None, # verify leaf node
  root.right.left == None, # verify leaf node
  root.right.right == None # verify leaf node
)
root = Node(6,
  Node(6,
    Node(6),
    Node(6)),
  Node(6))
treeFlip(root)
print(
  root.value == 6,
  root.left.value == 6,
  root.right.value == 6,
  root.left.left == None, # verify leaf node
  root.left.right == None, # verify leaf node
  root.right.left.value == 6,
 
  root.right.left.left == None, # verify leaf node
  root.right.left.right == None, # verify leaf node
  root.right.right.left == None, # verify leaf node
  root.right.right.right == None # verify leaf node
)

#print(addEvenValuedParent(root) )              