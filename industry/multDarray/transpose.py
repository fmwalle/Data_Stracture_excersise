def transpose(matrix):
    outer=[]
    for i in range(len(matrix[0])):
        inner=[]
        for j in range(len(matrix)):
           inner.append(matrix[j][i])
        outer.append(inner)   
         
    return outer
matrix=[[1,2,3,4],[5,6,7,8]]
print(transpose(matrix))      
    