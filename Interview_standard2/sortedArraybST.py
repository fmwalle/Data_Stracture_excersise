class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


def change_Bst(array):
    if not array:
        return None

    mid =len(array)//2
    root=TreeNode(array[mid]) 

    root.left=change_Bst(array[:mid])
    root.right=change_Bst(array[mid+1:])
    return root   
def pre_order(root):
    if not root:
        return []
    array=[]
    def dfs(node):
     if not node :
         return
     nonlocal array
     array.append(node.value)
     dfs(node.left)
     dfs(node.right)
    dfs(root) 
    return array
nums = [-10, -3, 0, 5, 9]
root = change_Bst(nums)
pre_order_result = pre_order(root)
print(pre_order_result)  