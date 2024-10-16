from collections import deque
class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def buildTree(adj_lists):
    '''
    it is about creating a tree from adjusent list.
    we take list size as node
    and put the each lists member as a left child and right child

    
    '''    
    # create anode for each 
    nodes=[]
    for i in range(len(adj_lists)):
        node=TreeNode(i)
        nodes.append(node)


    # attch node to children
    for i ,children in enumerate(adj_lists):
        if len(children)>0:
            nodes[i].left=nodes[children[0]]
        if len(children)>1:
            nodes[i].right=nodes[children[1]]  
    return nodes[0]  
root = buildTree([
    [1, 2],  # Node 0: children 1 and 2
    [3],     # Node 1: child 3
    [],      # Node 2: no children
    []       # Node 3: no children
])
def printTree(node, level=0):
    if node:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.left, level + 1)

printTree(root)        


def deletenodes(root,to_delete_list):
     deletedset=set(to_delete_list)
     forest=[]
     def dfs(node,isroot):
         if not node:
             return None
         
         node_deleted=node.value in deletedset

         if isroot and not node_deleted:
             forest.append(node)

         node.left=dfs(node.left,node_deleted)
         node.right=dfs(node.right,node_deleted)  

         return None if node_deleted else node  

     dfs(root,True) 
     return forest   

def treeToArray(root):
    if not root:
        return []
    
    result=[]
    queue=deque([root])

    while queue:

        node=queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
print(treeToArray(None), []);
print(treeToArray(TreeNode("a", TreeNode("b", TreeNode("c"), TreeNode("d")))))
print(treeToArray(TreeNode("a", TreeNode("b", TreeNode("c", TreeNode("d"))))))        


