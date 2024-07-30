def isMonotonic(nums: list[int]) -> bool:


    dec=True
    inc=True
    for i in range(1,len(nums)):
        dec=dec and nums[i]<=nums[i-1]
        inc=inc and nums[i]>=nums[i-1]
    return dec or inc    


print(isMonotonic([]))
print(isMonotonic([5]) )
print(isMonotonic([5,10]) )
print(isMonotonic([10,5]))
print(isMonotonic([1,5,5,10]))    
print(isMonotonic([4,2,8]) )
print(isMonotonic([8,2,4]) )    