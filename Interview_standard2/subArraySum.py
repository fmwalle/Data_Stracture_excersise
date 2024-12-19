def countSubarraySum(nums, k):
    if not nums:
        return []
    
    map_array={0:1}
    count=0
    sum=0
    for num in nums:
        sum+=num
        if sum-k in map_array:
            count+=map_array[sum-k]
        if sum in map_array:
            map_array[sum] += 1
        else:
            map_array[sum] = 1

    return count

print(countSubarraySum([1, 1, 1], 2) == 2) 
print(countSubarraySum([1, 2, 3, -1, 4], 3) == 3)     


    