class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def findMax(root):

    if not root:
        return float('-inf')

    left_max=findMax(root.left)
    
    right_max=findMax(root.right)
 


    return max(root.value,left_max,right_max)   
def countElemntsInBineryTree(root):
     if not root:
         return 0
     left_count=countElemntsInBineryTree(root.left)
     right_count=countElemntsInBineryTree(root.right)

     return 1 +left_count + right_count
def uniValued(root):
    if not root :
        return True
    def checkValues(root,value):
       if not root:
           return True   
       if root.value!=value:
           return False
       return checkValues(root.left,value) and checkValues(root.right,value)

    return checkValues(root,root.value)
def isUnivalTree( root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def uniHelper(node,val):
            if not node:
                return True
              
            if node.value!=val:
                return False    
            leftnode= uniHelper(node.left,val)
           
            rightnode=uniHelper(node.right,val)
        

            return leftnode and rightnode
        return uniHelper(root,root.value) 


root=Node(1)
root.left=Node(1)
root.right=Node(1)
root.left.left=Node(1)
root.left.right=Node(1)
root.right.left=Node(1)
root.right.right=Node(2)

print(isUnivalTree(root))