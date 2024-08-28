class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def totalNodes(root):
    if not root:
        return 0

    return 1+totalNodes(root.left)+totalNodes(root.right)  
def hight(root):
    if not root:
        return 0
    leftNode=hight(root.left)
    righrNode=hight(root.right)
    return 1+max(leftNode,righrNode)    
def countLeafNode(root):
    if not root:
        return 0
    count=0
    def helperCount(root):
        if not root:
            return 0
        nonlocal count
        if not root.left and not root.right:
          count+=1
        helperCount(root.left)
        helperCount(root.right)
    helperCount(root)
    return count      
def sumAll(root):
    if not root:
        return 0
    
    return root.value+sumAll(root.left)+sumAll(root.right)
def countFullNodes(root):
    if not root:
        return 0
    count=0
    def helperfull(node):
        if not node:
            return 0
        nonlocal count
        if node.left and node.right:
            count+=1
        helperfull(node.left)
        helperfull(node.right)
    helperfull(root)
    return count    
def countOneChiled(root):
    if not root:
        return 0
    count=0
    def helperone(node):
        if not node:
            return 0
        nonlocal count
        if node.left and not node.right or node.right and not node.left:
              count+=1
        helperone(node.left)
        helperone(node.right) 
    helperone(root)
    return count        

def findMax(root):
    if not root:
        return float('-inf')
    leftNode=findMax(root.left)
    rightNode=findMax(root.right)

    return max(root.value,leftNode,rightNode)

def checkTrees(root1,root2):
    if not root1 and not root2:
        return True
    if not root2 or not root1:
        return False
    if root1 and root2 :
        if root1.value !=root2.value:
            return False
        
    return  checkTrees(root1.left,root2.left) and checkTrees(root1.right,root2.right)
def checkSameSubTree(root,subRoot):
    if not root and not subRoot:
        return True
    
    def checkSame(node1,node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.value !=node2.value:
            return False
        return checkSame(node1.left,node2.left) and checkSame(node1.right,node2.right)
    
    stack=[root]
    while stack:
        currentNode=stack.pop()
        if currentNode is None:
            continue
        if currentNode.value==subRoot.value:
           return checkSame(currentNode,subRoot) 
        stack.append(root.left)
        stack.append(root.right)
    return False    