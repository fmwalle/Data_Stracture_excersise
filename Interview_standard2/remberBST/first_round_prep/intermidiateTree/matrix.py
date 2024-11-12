def linearizeRowMajor(matrix):
    
    result=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result.append(matrix[i][j])
    return result 
def findaverages(matrix):
    sum_col=0
    sum_row=0
   
    smallest_row=float('inf')

    for i in range(len(matrix[0]))  :
        smallest_col=float('inf')
        for j in range(len(matrix)) :
            if matrix[j][i]<smallest_col:
                smallest_col=matrix[j][i]
        sum_col+=smallest_col
      
    print(sum_col/len(matrix[0]))
    for i in range(len(matrix)):
        smallest_row=float('inf')
        for j in range(len(matrix[i])):
            if matrix[i][j]<smallest_row:
                smallest_row=matrix[i][j]

        sum_row+=smallest_row
    print(sum_row/len(matrix))            




matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
print(findaverages(matrix))
print(linearizeRowMajor(matrix))