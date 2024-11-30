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

#print(twoSum([2,7,11,15],9))    

def threeSum(nums):
    if len(nums)<3:
        return []

    answer=[]
    for i in range(0,len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1

        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum==0:
                answer.append(nums[i])
                answer.append(nums[left])
                answer.append(nums[right])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                      right-=1
            elif sum<0:
                left+=1
            else:
                right-=1              
    return answer
print(threeSum([-1,0,1,2,-1,-4]))

