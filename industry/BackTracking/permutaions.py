from itertools import permutations
def permuteUnique(nums):

  set_perm=set(permutations(nums))
  perm=[]
  for i in set_perm:
    perm.append(i)
  return perm  
def understandPerm(s):
  
  set_perm=[]
  for i in range(1,len(s)+1):
   for perm in permutations(s,i):
        set_perm.append(perm)
  return set_perm  

print(understandPerm("ABC"))

def permutaionsbuild(nums):

  result=[]
  def helpdfs(start):
    if start==len(nums):
      result.append(nums[:])
    else:

      for i in range(start,len(nums)):

        nums[start],nums[i]=nums[i],nums[start]

        helpdfs(start+1)

        nums[start],nums[i]=nums[i],nums[start]

  helpdfs(0)
  return result

print(permutaionsbuild([2,2,2]))
        