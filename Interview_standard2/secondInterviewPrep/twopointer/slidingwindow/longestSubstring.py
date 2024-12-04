#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    l=0
    length=0
    setchars=set()
    n=len(s)
    for r in range(n):
        while s[r] in setchars:
            setchars.remove(s[l])
            l+=1

        setchars.add(s[r])
        windo=(r-l)+1
        length=max(windo,length)    

    return length
print(lengthOfLongestSubstring('abcabcbb'))    

'''
Maximum Sum of a Subarray of Size K
Problem: Given an array of integers arr and an integer k, find the maximum sum of any contiguous subarray of size k.
Example:
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (The subarray is [5, 1, 3])
Hint: Maintain a running sum of the current window, and slide the window one element at a time.
Longest Substring of All 1s After Replacing at Most K Zeros
Problem: Given a binary array nums and an integer k, find the length of the longest contiguous subarray containing only 1s after replacing at most k 0s.
Example:
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0], k = 2
Output: 7
Hint: Track the count of zeros in the window. If zeros exceed k, shrink the window.


'''

#https://leetcode.com/problems/longest-repeating-character-replacement/description/

def characterReplacement(s,k):
    count=[0]*26
    longest=0
    l=0

    for r in range(len(s)):
        count[ord(s[r])-65]+=1

        while r-l+1 -max(count)>k:
            count[ord(s[l])-65]-=1
            l+=1

        longest=max(longest,(r-l)+1)
    return longest

print(characterReplacement('ABAB',2))    


print(characterReplacement('AABAAC',2)) 
