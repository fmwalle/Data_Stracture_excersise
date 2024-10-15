from collections import deque
class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def isSymmetric(root):

    if not root:
        return True

    queue=deque([(root.left,root.right)])

    while queue:
        nodeleft,noderight=queue.popleft()


        if not nodeleft and not noderight:
            continue

        if not nodeleft or not noderight or noderight.value!=nodeleft.value:
            return False
        
        queue.append((nodeleft.right,noderight.left))
        queue.append((nodeleft.left,noderight.right))
    return True    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))

def issymetric_recursively(root):

    if not root : 
        return True
    
    def helpbfs(leftnode,rightnode):

        if not leftnode and not rightnode:
            return True
        if not leftnode or not rightnode:
            return False
        
        return leftnode.value==rightnode.value and helpbfs(leftnode.left,rightnode.right) and helpbfs(leftnode.right,rightnode.left)
    return helpbfs(root.left,root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(issymetric_recursively(root))

def bfs(root):
    if not root :
        return []
    
    queue=deque([root])
    result=[]

    while queue:
        node=queue.popleft()

        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result            