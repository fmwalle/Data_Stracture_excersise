class Node:
    def __init__(self,value,right=None,left=None):
        self.value=value
        self.left=left
        self.right=right

def invertTree(root:Node):
    if not root:
        return None
    
    root.left,root.right=root.right,root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


      

