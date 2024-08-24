from collections import deque
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def bfs(root):
   if not root:
       return []
   queue=deque([root])
   answer=[]
   while queue:
        currentNode=queue.popleft()
        answer.append(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)   
   return answer   

complete = Node('a',
  Node('b',
    Node('d'),
    Node('e')
  ),
  Node('c',
    Node('f'),
    Node('g')
  )
)      
print(bfs(complete))