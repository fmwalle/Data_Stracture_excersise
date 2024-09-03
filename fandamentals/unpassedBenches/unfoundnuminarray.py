def unfoundNum(nums:list[int])->int:
    numsLen=len(nums)
    if numsLen not in nums:
        return numsLen
    for i in nums:
        num=numsLen-i
        if num not in nums:
            return num
    return -1

print(unfoundNum([1,1]))    