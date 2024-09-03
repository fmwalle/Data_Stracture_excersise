class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
        # inorder= (left,root,right)
def inorderTraversal(root) :
    res=[]
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.value)
        inorder(root.right)
    inorder(root)
    return res           
def inorderTraversalItertively(root):

    res=[]
    stack=[]
    curr=root
    while curr or stack:
      while curr:
          stack.append(curr.value)
          curr=curr.left
      curr=stack.pop()  
      res.append(curr.value)
      curr=curr.right  
    return res 
def preorder(root):
    curr,stack=root,[]
    res=[]
    while curr or stack:
        if curr :
            res.append(curr.value)
            stack.append(curr.right)
            curr=curr.left 
        else:
         curr=stack.pop()
