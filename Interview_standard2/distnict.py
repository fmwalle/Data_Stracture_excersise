class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def treeIsImmediatelyDistinct(root: TreeNode) -> bool:
    if not root or not root.left or not root.right:
        return True
    
    def dfshelper(node):
        if not node:
            return True
        
        if node.left and node.left.value==node.value:
            return False
        
        if node.right and node.right.value==node.value:
            return False
  
        
        return dfshelper(node.left) and dfshelper(node.right)
        

    return dfshelper(root)

print(treeIsImmediatelyDistinct(None) is True)

#    1
#  1   2
# 3 4    6
root = TreeNode(1,
        TreeNode(1,
          TreeNode(3),
          TreeNode(4)
          ),
        TreeNode(2,
          None,
          TreeNode(6)
          )
        )
print(treeIsImmediatelyDistinct(root) is False)

#    1
#  2   2
# 5 9
root = TreeNode(1,
        TreeNode(2,
          TreeNode(5),
          TreeNode(9)
          ),
        TreeNode(2)
        )
print(treeIsImmediatelyDistinct(root) is True)

#  2
# 5 9
root = TreeNode(2,
        TreeNode(5),
        TreeNode(9))
print(treeIsImmediatelyDistinct(root) is True)

# 2
root = TreeNode(2)
print(treeIsImmediatelyDistinct(root) is True)

#  1
# 5 1
root = TreeNode(1,
        TreeNode(5),
        TreeNode(1))
print(treeIsImmediatelyDistinct(root) is False)

#  1
# 2 2
root = TreeNode(1,
        TreeNode(2),
        TreeNode(2))
print(treeIsImmediatelyDistinct(root) is True)

#    1
#  2
# 1
root = TreeNode(1,
        TreeNode(2,
          TreeNode(1)
          )
        )
print(treeIsImmediatelyDistinct(root) is True)

#    1
#  1
# 1 1
root = TreeNode(1,
        TreeNode(1,
          TreeNode(1),
          TreeNode(1)
          )
        )
print(treeIsImmediatelyDistinct(root) is False)

#    6
#  8
# 4 8
root = TreeNode(6,
        TreeNode(8,
          TreeNode(4),
          TreeNode(8)
          )
        )
print(treeIsImmediatelyDistinct(root) is False)

#    6
#   8
#  4
# 8
root = TreeNode(6,
        TreeNode(8,
          TreeNode(4,
            TreeNode(8)
            )
          )
        )
print(treeIsImmediatelyDistinct(root) is True)

#    6
#   8
#  4
# 6
root = TreeNode(6,
        TreeNode(8,
          TreeNode(4,
            TreeNode(6)
            )
          )
        )
print(treeIsImmediatelyDistinct(root) is True)
           