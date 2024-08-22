class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def insertElemnt(root,val):
    if not root:
        return Node(val)

    if val< root.value:
        if root.left is None:
            root.left=Node(val)
        else:
            insertElemnt(root.left,val)
    elif val> root.value:
        if root.right is None:
            root.right=Node(val) 
        else:
            insertElemnt(root.right,val)  
    return root  
def isvalid(root)->bool:
    if not root:
        return True
    def valid(root,min,max):
        if not root:
            return True
        if not (min<root<max):
            return False
        return valid(root.left,min,max) and valid(root.right,min,max)   
    return valid(root,float('-inf'),float('inf'))

 
         
def printing(root):
    if not root:
        return None
    currentVal=root.value
    print(currentVal,end="->")
    printing(root.left)
    printing(root.right)

root = Node(10)
insertElemnt(root, 5)
insertElemnt(root, 15)
insertElemnt(root, 2)
insertElemnt(root, 12)   
                 
print(isvalid(insertElemnt(root,19)))
print(printing(insertElemnt(root,19)))               