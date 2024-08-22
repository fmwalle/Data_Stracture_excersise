from collections import deque
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def deleteNode(root,key):
    if not root:
        return
    queue=deque()
    queue.append(root)

    while queue:
        currentNode=queue[0]
        if currentNode.value==key:
            queue.popleft()
        if root.left:
            queue.append(root.left) 
        if root.right:
            queue.append(root.right)    
    return queue     

    