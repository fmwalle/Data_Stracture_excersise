from collections import deque
def countLiberties(board,x,y):
    row,col=len(board),len(board[0])
    target_point=board[x][y]

    if target_point=='+':
        return 0
    
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    visited=set()
    libretes=set()
    queue=deque([(x,y)])
    while queue:
        cx,cy=queue.popleft()
        if (cx,cy) in visited:
            continue
        visited.add((cx,cy))
        for dx,dy in directions:
          nx,ny=cx+dx,cy+dy

          if 0<=nx<=row and 0<ny<col:
            if board[nx][ny]=='+':
                libretes.add((nx,ny))

            elif board[nx][ny]==target_point and (nx,ny )not in visited: 
                queue.append((nx,ny))   
    return len(libretes)  

board1 = [
    ['+', '+', 'W', '+', '+', '+'],
    ['+', '+', 'W', '+', '+', '+'],
    ['+', '+', 'W', 'W', '+', '+'],
    ['+', '+', '+', 'W', 'W', '+'],
    ['+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+']
]

print(countLiberties(board1, 2, 2))  # Output: 10
