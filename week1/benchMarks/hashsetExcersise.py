def solution(nums):
    numsSet=set()
    
    for i in range(1,len(nums)+1):
        numsSet.add(i)
    print(numsSet)    
    for values in numsSet:
        if values not in nums:
            return values
    return -1 

print(solution([1,2,2]))