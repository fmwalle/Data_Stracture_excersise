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


def permutation(nums):
    if len(nums)==0:
        return [[]]
    result=[]
    def dfs(start):
        if start>=len(nums):
            result.append(nums[:])
            return
        for i in range(start,len(nums)):
            nums[i],nums[start]=nums[start],nums[i]

            dfs(start+1)
            nums[i],nums[start]=nums[start],nums[i]

    dfs(0)
    return result
print(permutation([1,2,3]))

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letter_combination(digits):
    if not digits:
        return []
    
    digit_to_char_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
        } 
    result=[]

    def dfs(index,combination):
        if len(combination)==len(digits):
            result.append(''.join(combination))
            return
        
        digit=digits[index]
        values=digit_to_char_map[digit]

        for chr in values:
            combination.append(chr)

            dfs(index+1,combination)
            combination.pop()
    dfs(0,[])
    return result        

print(letter_combination('23'))