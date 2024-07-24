def indicesOfTarget(arr: list[int], target: int):
  indcise=[]
  index=0
  for number in arr:
   if number==target :
    
    indcise.append(index)

    
   index+=1
  return indcise  
     
     
  
  
print(indicesOfTarget([20,30,30],30))

def isMonotonic(nums):
    inc=True
    dec=True
    for i in range(1,len(nums)):
        inc= inc and nums[i-1]<=nums[i]
        dec= dec and nums[i-1]>=nums[i]

    return inc or dec    

print(isMonotonic([1,2,3,4,1]))  
def count_anagram_groups(words):
    anagram_groups = {}
    
    for word in words:
        # Sort the word to create a key for the anagram group
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        
        # Use the sorted word as the key in the dictionary
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    
    # The number of groups is the number of unique keys in the dictionary
    return len(anagram_groups)

# Example usage
words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]
result = count_anagram_groups(words)
print(result)    
