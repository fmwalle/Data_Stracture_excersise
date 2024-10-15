
from collections import deque
def bfs(maze):

    goal_value='4'
    start=(0,0)
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    visted=set()
    visted.add(start)

    queue=deque([(start,[(0,0)])])
    while queue:
        (currentpostion, path)=queue.popleft()
        x,y=currentpostion
        if maze[x][y]==goal_value:
            return path
        
        for direction_row,direction_colomn in directions:
            newrow=direction_row+x
            newcol=direction_colomn+y
            newpostion=(newrow,newcol)
            
            if is_valid_direction(newrow,newcol)and newpostion not in visted:
                visted.add((newrow,newcol))

                queue.append([(newrow,newcol),path+[newpostion]])
    return None            

def is_valid_direction(x,y)  :
    return 0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y] not in [' ','5']          
maze = [
    ['5', ' ', ' ', 'A', ' '],
    ['B', 'C', 'D', 'E', ' '],
    [' ', ' ', 'F', ' ', '4'],
    ['G', 'H', 'I', ' ', 'J'],
    ['K', ' ', 'L', 'M', 'N'],
]
# find the direction to 4 from 5. a space is a block or wall .validity is either number or letter

print(bfs(maze))