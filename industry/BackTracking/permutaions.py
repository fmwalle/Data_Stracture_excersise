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
  def helpdfs(start,end):
    if start==end:
      result.append(nums[:])
    else:

      for i in range(start,end):

        nums[start],nums[i]=nums[i],nums[start]

        helpdfs(start+1,end)

        nums[start],nums[i]=nums[i],nums[start]

  helpdfs(0,len(nums))
  return result

print(permutaionsbuild([1,2,3]))
        