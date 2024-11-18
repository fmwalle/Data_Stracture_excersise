'''https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/'''

def xor(nums):
    def dfs(index,total):
        if index==len(nums):
            return total
        
        return dfs(index+1,total^nums[index])+dfs(index+1,total)
    
    return dfs(0,0)

print(xor([5,1,6]))

# https://leetcode.com/problems/subsets/description/
def subset(nums):
    result=[]
    subset=[]
    def dfs(index):
        if index >=len(nums):
            result.append(subset[:])
            return
        # descion of include
        subset.append(nums[index])
        dfs(index+1)  
        # descion of exclude
        subset.pop()
        dfs(index+1)

    dfs(0)
    return result

print(subset([1,2,3]))      


# https://leetcode.com/problems/combination-sum/description/

def combination_sum(nums,target):
    result=[]
    def dfs(index,subset,total):
        if total==target:
            result.append(subset[:])
            return
        
        if index>=len(nums) or total>target:
            return
        
        # descion of include
        subset.append(nums[index])
        dfs(index,subset,total+nums[index])
        # descion of exclude
        subset.pop()
        dfs(index+1,subset,total)

    dfs(0,[],0)
    return result


print(combination_sum([2,3,6,7],7))

