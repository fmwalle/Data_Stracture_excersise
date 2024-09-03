def linearizeRowMajor(array):
    answer=[]
   
    for i in range(len(array)):
       for j in range(len(array[i])):
          answer.append(array[i][j])
    return answer        
def linearizeColumnMajor(matrix: list[list[int]]) -> list[int]:
  result = []
  for i in range(len(matrix[0])):
    for j in range(len(matrix)):
      result.append(matrix[j][i])
  return result
def averageRowMinimum(array):
     if len(array) == 0 or len(array[0]) == 0:
      return 0
      
     sum=0
     for i in range(len(array)):
       smallest=float('inf')
       for j in range(len(array[i])):
         val=array[i][j]
         if val<smallest:
            smallest=val
       sum+=smallest
     return sum/len(array)  
def averageColumnMinimum(array):
   if len(array) == 0 or len(array[0]) == 0:
      return 0
   sum=0
   for i in range(len(array[0])):
        smllest=float('inf')
        for j in range(len(array)):
           val=array[j][i]
           if val<smllest:
            smllest=val
        sum+=smllest
   return sum/len(array[0])        
          
matrix = [[]]
print(averageColumnMinimum(matrix) == 0)
#print(averageRowMinimum(matrix) == 0)

matrix = [[5]]
print(averageColumnMinimum(matrix) == 5)
#print(averageRowMinimum(matrix) == 5)

matrix = [[1, 2, 3]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 1)

matrix = [
  [1],
  [4],
  [7]]
print(averageColumnMinimum(matrix) == 1)
#print(averageRowMinimum(matrix) == 4)    

matrix = [[]]
print(linearizeRowMajor(matrix) == [])
print(linearizeColumnMajor(matrix) == [])

matrix = [[1]]
print(linearizeRowMajor(matrix) )
print(linearizeColumnMajor(matrix) == [1])

matrix = [[1, 2, 3]]
print(linearizeRowMajor(matrix) )
print(linearizeColumnMajor(matrix) == [1,2,3])   
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
print(linearizeRowMajor(matrix) )
print(linearizeColumnMajor(matrix) == [1,4,7,2,5,8,3,6,9])
