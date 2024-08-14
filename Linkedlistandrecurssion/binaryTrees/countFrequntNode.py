class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def height(root) -> int:
    if not root:
        return 0
    
    # Debug prints to show the traversal order
    print("Before calculating left height")
    lefthight = height(root.left)
    print(f"Left height of node with value {root.value}: {lefthight}")
    
    print("Before calculating right height")
    rightheight = height(root.right)
    print(f"Right height of node with value {root.value}: {rightheight}")

    # Return the height of the current node
    return max(lefthight, rightheight) + 1

root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.left.left=Node(4)
root.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print(height(root))
