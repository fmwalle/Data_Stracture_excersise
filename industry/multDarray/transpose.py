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
def linearizeRowMajor(matrix):
    answer=[]
    for i in range(len(matrix)):
       for j in range(len(matrix[i])):
           answer.append(matrix[i][j])
    return answer       

def linearizeColumnMajor(matrix):
     answer=[]
     for i in range(len(matrix[0])):
         for j in range(len(matrix)):
             answer.append(matrix[i][j])

     return answer   
def averageColumnMinimum(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
    
    sum=0
    for i in range(len(matrix[0])):
        minValue=float('inf') 
        for j in range(len(matrix)):
           minValue=min(minValue,matrix[j][i])
        sum+=minValue
    return sum/len(matrix[0])
def averageRowMinimum(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return 0
    total=0
    for i in range(len(matrix)):
        miniVal=float('inf')

        for j in range(len(matrix[i])):
            miniVal=min(miniVal,matrix[i][j])
        total=total+miniVal
    return total/len(matrix)        


matrix = [[]]
print(averageColumnMinimum(matrix) == 0)
print(averageRowMinimum(matrix) == 0)

matrix = [[5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)

matrix = [[1, 2, 3]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 1)

matrix = [
  [1],
  [4],
  [7]]
print(averageColumnMinimum(matrix) == 1)
#print(averageRowMinimum(matrix) == 4)     
