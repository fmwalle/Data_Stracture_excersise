def rotateLeft(nums: list[int], k: int) -> list[int]:
   lengthofarray=len(nums)
   k=k%lengthofarray

   def reverse(nums, start,end):
      nums[start],nums[end]=nums[end],nums[start]
      start+=1
      end-=1

   reverse(nums,0,k-1)
   reverse(nums,k,lengthofarray-1)
   reverse(nums,0,lengthofarray-1)  

   return nums  


print(rotateLeft([1,2,3,4], 0))
print(rotateLeft([1,2,3,4], 1))
print(rotateLeft([1,2,3,4], 2))
print(rotateLeft([2,4,6,8,10], 6))
print(rotateLeft([2,4,6,8,10], 10))