def containsDuplicate(nums):
    if not nums:
        return False
    my_set=set(nums)
    return len(my_set)==len(nums)