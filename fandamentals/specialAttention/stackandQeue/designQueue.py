def printDoc(actions:list)->list:
    queue=[]
    printed=[]
    for action in actions:
        if action[0]=="add":
            queue.append(action[1])
        elif action[0]=="print":
            if queue:
                printed.append(queue.pop())    
        elif action[0]=="cancel":
            if action[1] in queue:
                queue.remove(action[1])   
    return printed             

actions = [
    ("add", "doc1"),
    ("add", "doc2"),
    ("print",),
    ("print",)
]
result = printDoc(actions)
print(result)  