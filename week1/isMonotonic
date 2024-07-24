def isPerfectWeave(deck: list[str]):

    if len(deck)%2!=0 : return False
    rb =True
    br=True

    for i in range(0,len(deck),2):
        if(i+1<len(deck)):
            rb=rb and deck[i]=='R' and deck[i+1]=='B'
            br= br and deck[i]=='B' and deck[i+1]=='R'

    return rb or br        

print(isPerfectWeave(["B", "B", "R", "B", "R"]))  
print(isPerfectWeave(["R", "B", "R", "B", "B"]))  
print(isPerfectWeave(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B"])) 
def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Initialize the two pointers
    j = 0
    
    # Traverse the array
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    
    # The length of the unique array
    return j + 1

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)
print("Length of array after removing duplicates:", length)
print("Array after removing duplicates:", arr[:length])  