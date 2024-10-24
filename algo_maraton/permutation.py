def permutate(nums):
     
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       # store all permuation val
        # store a perm that doesn't duplicate

        result = []
        counter={}
        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1    
        def backtrack(perm, counter):
            if len(perm)==len(nums):
                result.append(perm[:])
                return

            for keys in counter:
                if counter[keys]==0:
                    continue
                perm.append(keys)
                counter[keys]-=1
                backtrack(perm,counter)
                perm.pop()
                counter[keys]+=1

        backtrack([],counter)                

        return result

print(permutate([1,1,2]))