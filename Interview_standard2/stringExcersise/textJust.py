def fullJustify(words, maxWidth):
    if not words or maxWidth==0:
        return []
    
    result=[]

    count=0
    current_sentence=''
    for word in words:
      if len(current_sentence)+len(word)+1>maxWidth:
         result.append(current_sentence.strip())
         current_sentence=word
      else:
         current_sentence+=' '+word   

    if current_sentence:
       result.append(current_sentence)    

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
max_length = 15
print(fullJustify(words,16))


# find minimum and maximum recursively 
def findMin(arr: list[int]) -> int:
   mini=float('inf')

   def helper(arr,index):
      nonlocal mini
      if index>=len(arr):
         return 
      if arr[index]<mini:
         mini=arr[index]
      helper(arr,index+1)
   helper(arr,0)
   return mini     
      
   
def findMax(arr: list[int]) -> int:
   maxi=float('-inf')

   def helper(arr,index):
      nonlocal maxi
      if index>=len(arr):
         return 
      if arr[index]>maxi:
         maxi=arr[index]
      helper(arr,index+1)
   helper(arr,0)
   return maxi    
def findMini2(arr:list[int]):
   if len(arr)==1:
      return arr[0]
   return min(arr[0],findMini2(arr[1:]))
      
print(findMini2([15,3,5,1,0]))