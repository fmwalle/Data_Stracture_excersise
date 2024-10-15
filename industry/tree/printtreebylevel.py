class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def print_by_level(root):# we do this based on bfs

    if not root:
        return []
    result=[]
    queue=[root]

    while queue:
        level=[]
        next_queueu=[]


        for node in queue:
            level.append(node.value)

            if node.left:
                next_queueu.append(node.left)
            if node.right:
                next_queueu.append(node.right)
        result.append(level) 
        queue=next_queueu
    return result
root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print(print_by_level(root ))  

def print_zigzag_by_level(root):

    if not root:
        return []
    result=[]
    queue=[root]

    level=0
    left_right=True
    while queue:
        level=[]
        next_queue=[]
        
        for node in queue:
            level.append(node.value)
        
       
            if node.left:
                next_queue.append(node.left)  
            if node.right:
                next_queue.append(node.right)
        if not left_right:
            level.reverse()        
        result.append(level)
        queue=next_queue
        left_right=not left_right
    return result
root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
print(print_zigzag_by_level(root ))  
                             