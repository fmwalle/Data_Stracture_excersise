class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def checkOneChild(root):
  parents=[]  
  def dfs(node):
    if not node:
      return []

    if node.left and not node.right:
      parents.append(node.value)  
    elif not node.left and node.right:
      parents.append(node.value)

    dfs(node.left)
    dfs(node.right)

  dfs(root)
  return parents        
def isDirectReport(root,e1,e2):
   if not root:
      return False
   if root.value==e1:
      if root.left and root.left.value==e2 or root.right and root.right.value==e2:
         
            return True
    
   isDirectReport(root.left,e1,e2) 
   isDirectReport(root.right,e1,e2) 
   return False     

root = Node(1,
  Node(2,
    None,
    Node(4)),
  Node(3))
print(set(checkOneChild(root)) == set([2]))
ceo = Node(1,
        Node(2),
        Node(3,
          Node(4,
            Node(6)),
          Node(5)
      ))
partner = Node(5,
            Node(10)
          )
def findElemntintree(root,target):
   if not root:
      return False
   if root.val==target:
      return True
   return findElemntintree(root.left,target)  and findElemntintree(root.right,target) 
# here is the binary search tree
def bst(root,target):
  if target==root.val:
     return True
  if target<root.val:
     return bst(root.left,target)
  elif target > root.val:
     return bst(root.right,target)
      
print(isDirectReport(partner, 5, 10))
print(isDirectReport(ceo, 1, 2) )
print(isDirectReport(ceo, 1, 4))
