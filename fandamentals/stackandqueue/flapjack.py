def freshFlapjacks(pancakes : list[int]):

    isvalid=True
    maxHeight=0
    currentHeight=0
    for i in range(len(pancakes)):
        currentHeight=currentHeight+pancakes[i]
        if currentHeight<=0:
            isvalid=False
        maxHeight= max(currentHeight,maxHeight)
        
        if maxHeight>4:
            isvalid=False
    return [isvalid,maxHeight]    

print(freshFlapjacks([2, -1, 3, -3, 2, -1]))    


def desgignaque(actions):

    queue=[]

    while actions:
        if actions[0]=="add":
            queue.append(actions[1])
        elif     