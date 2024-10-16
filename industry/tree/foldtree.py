from collections import deque
class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def folding(root):
    if not root:
        return None
    # when i need to create atrree from another tree
    foldingTree = TreeNode(root.value)

    def dfs(left,right):
        if not left and not right:
            return None
        val=(left.value if left else 0 )+(right.value if right else 0)
        newNode=TreeNode(val)

        newNode.left=dfs(left.left if left else None,right.right if right else None)
        newNode.right=dfs(left.right if left else None,right.left if right else None)
        return newNode
    #foldingTree = TreeNode(root.value)
    foldingTree.left = dfs(root.left, root.right)

    return foldingTree


def compareTrees(a, b):
  if not a and not b:
    return True
  elif not a or not b:
    return False
  else:
    return a.value == b.value \
    and compareTrees(a.left, b.left) \
    and compareTrees(a.right, b.right)

example = TreeNode(1,
  TreeNode(2,
    TreeNode(4),
    TreeNode(5)),
  TreeNode(3,
TreeNode(6),
    TreeNode(7)))

expectedFolded = TreeNode(1,
TreeNode(5,
    TreeNode(11),
    TreeNode(11)))
print(compareTrees(folding(example), expectedFolded))

print(compareTrees(folding(None), None))

