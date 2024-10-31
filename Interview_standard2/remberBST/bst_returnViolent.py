class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def findViolet(root):
    if not root:
        return -1
    
    violent=-1
    def dfs_help(node,min_val,max_val):
        if not node:
            return 
        nonlocal violent

        if not (min_val<node.value<max_val):
            violent=node.value
            return

        dfs_help(node.left,min_val,node.value)
        dfs_help(node.right,node.value,max_val)

    dfs_help(root,float('-inf'),float('inf'))
    return violent      

def max_sum(root):
    if not root:
        return 0
    def dfs_help(node):
        if not node:
            return 0

        left_path=dfs_help(node.left)
        right_path=dfs_help(node.right)

        return  node.value+max(right_path,left_path)  
    return dfs_help(root)