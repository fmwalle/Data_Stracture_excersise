from collections import deque
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def isSameTree(root1,root2)->bool:
    if  not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    return (root1.value==root2.value and 
     isSameTree(root1.left,root2.left) 
      and isSameTree(root1.right,root2.right))
def checkSubtree(root1, root2) -> bool:
    if not root2:
        return True  # An empty tree is always a subtree
    if not root1:
        return False  # Non-empty subtree can't match an empty tree
    if checkSubtree(root1, root2):
        return True
    return checkSubtree(root1.left, root2) or checkSubtree(root1.right, root2)
       

def findHight(root):
    if not root:
        return 0
    return 1+ max(findHight(root.left) ,findHight(root.right) )
def isIdentical(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    return root1.value==root2.value and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)   

def levelOrder(root):
    if not root:
        return []
    
    answer=[]
    queue=deque()
    queue.append(root)
    while queue:
        currentNode=queue.popleft()
        answer.append(currentNode.value)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    return answer            

def maxSumPath(root):
    if not root:
        return 0

    def summing(node,sum=0):
        if not node:
            return 0
     
           
        max(summing(root.left,sum+root.left.value), summing(root.right,sum+root.right.value )) 
        return summing(node,sum)   
               