def twoSum(array,target):
    result=[]
    left=0
    right=len(array)-1

    while left<right:
        if array[left]+array[right]==target:
            result.append(left+1)
            result.append(right+1)
        elif array[left]+array[right]<target :
            left+=1
        else:
            right-=1       
    return result

print(twoSum([2,7,11,15],9))    
