def generateSequence(target: int) -> list[list[int]]:
    if target==0:
        return [[]]
    result=[]
    for i in range(1,target+1):
        buildmatrix=[]
        for j in range(1,i+1):
            buildmatrix.append(j)

        result.append(buildmatrix)
    return result

print(generateSequence(3))        

