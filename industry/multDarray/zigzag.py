def linearizeZigZag(matrix):
    answer=[]

    for i in range(len(matrix)):
         for j in range(len(matrix[i])):
             if i%2!=0:
           
            
                answer.append(matrix[i][len(matrix[i])-1-j])
             else:
                 answer.append(matrix[i][j])   

   
    return answer  
def diagonalSum(matrix):

    total=0
    for i in range(len(matrix)):
        if i==len(matrix)-1-i:
            total+=matrix[i][i]
        else:
            total+=matrix[i][i]
            total+=matrix[i][len(matrix)-1-i]
    return total  
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonalSum(mat) == 25)

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
print(diagonalSum(mat) == 8)

mat = [[5]]
print(diagonalSum(mat) == 5)

mat = []
print(diagonalSum(mat) == 0)         
             
matrix = [[]]
print(linearizeZigZag(matrix) == [])

matrix = [[1]]
print(linearizeZigZag(matrix) == [1])

matrix = [[1, 2, 3]]
print(linearizeZigZag(matrix) == [1,2,3])

matrix = [
  [1],
  [4],
  [7]]
print(linearizeZigZag(matrix) == [1,4,7])

matrix=[[1,2,3,4],[5,6,7,8]]
print(len(matrix))