def countSubarraySum(nums, k):
    if not nums:
        return []
    count=0
    mapping={0:1}
    current_sum=0

    for num in nums:
        current_sum+=num
        if current_sum-k in mapping:
            count+=mapping[current_sum-k]
        mapping[current_sum]=mapping.get(current_sum,0)+1    

    return count

print(countSubarraySum([1, 1, 1], 2) == 2) 
print(countSubarraySum([1, 2, 3, -1, 4], 3) == 3)     


    