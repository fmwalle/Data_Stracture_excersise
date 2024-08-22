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
def findMostFrequentNodeValue(root):
    # create a dictionery class
        freq=dict()
    # add number of frequencyis in dictionery
        def helpFrequennt(node):
         if not node:
            return
         if node.value in freq:
          freq[node.value]+=1
         else:
          freq[node.value]=1
         if node.left:
          helpFrequennt(node.left)
         if node.right:
           helpFrequennt(node.right)
        helpFrequennt(root)    
        highestfreq=-1
        highestval=0
        for keys,val in freq.items():
         if val>highestfreq:
            highestfreq=val
            highestval=keys    
        return highestval  
 

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

def findMax(root):
    if not root:
        return float('-inf')
    leftNode=findMax(root.left)
    rightNode=findMax(root.right)

        

    return max(root.value,leftNode,rightNode) 
def countElemnt(root):
    if not root:
        return 0
    leftNode=countElemnt(root.left)
    rightNode=countElemnt(root.right)
    return 1+leftNode+rightNode


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(1)
root.left.right = Node(8)
root.right.right = Node(25)

print(countElemnt(root))
root = Node(5,
  Node(10,
    Node(1),
    Node(7)),
  Node(1))
print(findMostFrequentNodeValue(root))

