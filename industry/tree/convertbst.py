class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


def sortedArrayToBST(nums: list[int]) -> TreeNode:

    # first find the middle
    # then goes in to two 
    
    if not nums:
        return None
    length=len(nums)

    middle=length//2
    node=TreeNode(nums[middle])
    node.left=sortedArrayToBST(nums[:middle])
    node.right=sortedArrayToBST(nums[middle+1:])
    

    
    return node

def inorderTraversal(root):
    if not root :
        return None
    result=[]
    def dfsinorder(node):
        if not node:
            return
        
        
        dfsinorder(node.left)
        result.append(node.value)
        dfsinorder(node.right)
    dfsinorder(root)
    return result    
    

nums=[1,2,3,4,5]
print(inorderTraversal(sortedArrayToBST(nums)) )
                