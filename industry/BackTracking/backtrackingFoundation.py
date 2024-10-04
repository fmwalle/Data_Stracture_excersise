def findSubset(array,target):
    result=[]

    def helper(start,subset,sum):

        if sum==target:
            result.append(list(subset))
            return
        
        for i in range(start,len(array)):
           subset.append(array[i])
           helper(i+1,subset,array[i]+sum)
           subset.pop()
    helper(0,[],0)
    return result

print(findSubset([3, 34, 4, 12, 5, 2],9))  

def findAllPermutaions(array):

    result=[]

    def helpPermutaion(start):

       
        if start==len(array):
            result.append(array[:])
            return

        for i in range(start,len(array)):
             array[i],array[start]=array[start],array[i]
             helpPermutaion(start+1)

             array[i],array[start]=array[i],array[start]
            

    helpPermutaion(0,)
    return result         
print(findAllPermutaions([1,2,3]))

def 
                

