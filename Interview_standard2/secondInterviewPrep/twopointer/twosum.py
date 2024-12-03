def twoSum(array,target):
    result=[]
    left=0
    right=len(array)-1

    while left<right:
        if array[left]+array[right]==target:
            result.append(left+1)
            result.append(right+1)
        elif array[left]+array[right]<target :
            left+=1
        else:
            right-=1       
    return result

#print(twoSum([2,7,11,15],9))    

def threeSum(nums):
    if len(nums)<3:
        return []
    nums.sort()
    answer=[]
    for i in range(0,len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1

        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum==0:
                answer.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                      right-=1
            elif sum<0:
                left+=1
            else:
                right-=1              
    return answer
#print(threeSum([-1,0,1,2,-1,-4]))


def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        maximum=0
        while left<right:
            width=right-left
            curr_height=min(height[left],height[right])
            area=curr_height*width
            maximum=max(area,maximum)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maximum         
print(maxArea([1,8,6,2,5,4,8,3,7]))

def firstPalindrome(words):
    if not words:
        return ''

    for word in (words):
        left=0
        right=len(word)-1
        while left<right:
            if word[left]!=word[right]:
                break
            left+=1
            right-=1

        if left>=right:
            return word
    return " "   

print(firstPalindrome(["abc","car","ada","racecar","cool"]))      
print(firstPalindrome(["notapalindrome","racecar"]))  
print(firstPalindrome(["def","ghi"]))    

def fourSum(nums, target):
   result=[]
   nums.sort()
   for i in range(0,len(nums)-3):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,len(nums)-2):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        left=j+1
        right=len(nums)-1

        while left<right:
            total=nums[i]+nums[j]+nums[left]+nums[right]
            if total==target:
                result.append([nums[i],nums[j],nums[left],nums[right]])

                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1

                left+=1
                right-=1
            elif total<target:
                left+=1
            else:
                right-=1 
   return result                                  
print(fourSum([1,0,-1,0,-2,2],0))             






