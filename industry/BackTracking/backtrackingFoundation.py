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

#print(findSubset([3, 34, 4, 12, 5, 2],9))  

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
            

    helpPermutaion(0)
    return result         
#print(findAllPermutaions([1,2,3]))

def findAllSubset(array):
    result=[]
    def dfsHelp(start,currentSubset):
        result.append(currentSubset[:])

        for i in range (start,len(array)):
            currentSubset.append(array[i])
            dfsHelp(i+1,currentSubset)
            currentSubset.pop()
    dfsHelp(0,[])
    return result

print(findAllSubset([1,2,3]))        

def findPermution(array):
    result=[]
    def backtrackHelp(start):
        if start==len(array):
          result.append(array[:])
          return
        for i in range(start,len(array)):
            array[i],array[start]=array[start],array[i]
           
            backtrackHelp(start+1)
            array[i],array[start]=array[start],array[i]
    backtrackHelp(0)
    return result
print(findPermution([1,2,3]))    

def CombinationSum(array,target):

    result=[]
    def backtrack(currentSubset,reminigTraget,start):
        if reminigTraget==0:
            result.append(currentSubset[:])
            
        
        for i in range(start,len(array)):
            if array[i]>reminigTraget:
                continue
            currentSubset.append(array[i])

            backtrack(currentSubset,reminigTraget-array[i],i)

            currentSubset.pop()
    backtrack([],target,0)
    return result
print("combination sum")
print(CombinationSum([2,3,6,7],7))

def combinationsKdistnict(n,k):
    result=[]
    def backtrack(subset,start):
        if len(subset)==k:
            result.append(subset[:])

            return
        
        for i in range(start,n+1):
            subset.append(i)

            backtrack(subset,i+1)

            subset.pop()

    backtrack([],1)  
    return result
#print(combinationsKdistnict(4,2))

def letterNumberComb(digits):
    digit_to_char_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result=[]
    def generateCombination(nums,comb):
        if len(comb)==len(digits):
            result.append(comb)

            




        

                

