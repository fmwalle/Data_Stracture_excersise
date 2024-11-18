'''https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/'''

def xor(nums):
    def dfs(index,total):
        if index==len(nums):
            return total
        
        return dfs(index+1,total^nums[index])+dfs(index+1,total)
    
    return dfs(0,0)

print(xor([5,1,6]))

