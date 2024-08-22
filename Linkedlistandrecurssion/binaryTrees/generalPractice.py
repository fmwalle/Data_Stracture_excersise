class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def maxPath(root):
    #finding maximum path means finding max hight from the root
    if not root:
        return 0
    leftsubtree=maxPath(root.left)
    
    
    rightSubTree=maxPath(root.right)
        
   
    
    return max(leftsubtree,rightSubTree)+1
def validate(root):
    if not root:
        return True
    stack=[(root,float('-inf'),float('inf'))]
    while stack:
        currentNode,min,maxval=stack.pop()
        if not currentNode:
            continue
        val=currentNode.value
        if min>val or maxval<val:
            return False
        if currentNode.right:
            stack.append((currentNode.right,val,maxval))
        if currentNode.left:
          stack.append((currentNode.left,min,val))
         
       
           
    return True   
def maxSum(root):
    if not root:
        return 0
    totalmax=0
    leftNode=maxSum(root.left)
    rightNode=maxSum(root.right)
    totalmax=leftNode+rightNode
    return max(totalmax,root.value+leftNode+rightNode)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(maxPath(root))
        
   
              
