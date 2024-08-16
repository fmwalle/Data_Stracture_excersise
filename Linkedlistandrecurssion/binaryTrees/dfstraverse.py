#    a
#    /\
#    /   c
#    b   \f
#    / \
#    d  e
#
#depth first traverse output= abdecf

# to impleemnt depth first we shoild implemnt with stack
from collections import deque
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.right=right
        self.left=left
def dfs(root):
    if not root :
        return None
    stack=[root]
    count=0
    print("here")
    while stack:
       
        currentNode=stack.pop()
        print(currentNode.value)
        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:
            stack.append(currentNode.left)    

        
def bfs(root):
    if not root:
        return None
    queue=deque()
    queue.append(root)
    while queue:
        currentNode=queue.popleft()
        print(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)     
#definee the function
# check the base case
# using dfs or bfs find the value .
# if the value exist return True
# if the value not exist return false
def isfound(root,val):
    if not root:
        return False
    stack=[root]
    while stack:
        currentNode=stack.pop()
        if currentNode.value==val:
            return True
        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:   
            stack.append(currentNode.left) 
    return False  

def treeSum(root):
    if not root:
        return 0
    queue=deque()
    queue.append(root)
    sum=0
    while queue:
        currentNode=queue.popleft()
        sum+=currentNode.value
        if currentNode.left:
            queue.append(currentNode.left) 
        if currentNode.right:
            queue.append(currentNode.right) 
    return sum               
def miniValue(root):
    if not root:
        return float('-inf')  
    stack=[root]
    mini=float('inf')
    while stack:
        currentNode=stack.pop()
        if currentNode.value<mini:
            mini=currentNode.value
        if currentNode.left:
            stack.append(currentNode.left)
        if currentNode.right:
            stack.append(currentNode.right)
    return mini                

node =Node('a')
node.left=Node('b')   
node.right=Node('c')
node.left.left=Node('d')
node.left.right=Node('e')
node.right.right=Node('f')     
print(dfs(node)) 
print("**************here is BFS**********")
print(bfs(node))  
print(isfound(node,'j'))   
root =Node(11)
root.left=Node(12)   
root.right=Node(13)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6) 
print(treeSum(root))
print(miniValue(root))