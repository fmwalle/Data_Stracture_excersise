def rotateBy90(matrix):

    # do transpose
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    # reverse
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix      

def transpose(matrix):
    for i in range(len(matrix)):

        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix  

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 
print(transpose(matrix))

def findElemnt(matrix,target):
    row=0
    col=len(matrix[0])-1
    while row < len(matrix) and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            col-=1
        else:
            row+=1

    return False                      
def multiplication(matrixa,matrixb):
    # initialize result
    result=[[0]*len(matrixb) for _ in range(len(matrixa))]

    #loop through row of matrixa
    for i in range (len(matrixa)):
        #loop throgh colomon of matrix b
        for j in range (len(matrixb[0])):
            # loop throgh colomn of matrix a and or row of matrixb
            for k in range(len(matrixa[0])):
                result[i][j]+=matrixa[i][k]*matrixb[k][j]
    return result         

matrixa = [
    [1, 2],
    [3, 4]
]

matrixb = [
    [5, 6],
    [7, 8]
]

print(multiplication(matrixa, matrixb))

def turnIntoZeros(matrix):

    rowZeros=set()
    colZeros=set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                rowZeros.add(i)
                colZeros.add(j)

    for row in rowZeros:
        for j in range(len(matrix[0])) :
            matrix[row][j]=0
    for col in colZeros:
        for j in range(len(matrix)):
            matrix[j][col]=0
    return matrix        

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
print(turnIntoZeros(matrix))                 
