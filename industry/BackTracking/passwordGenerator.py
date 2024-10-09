def permutations(arr):
  permutations = []
  x = 0

  def backtrack(start):
    nonlocal x
    x += 1

    if start == len(arr):
      permutations.append(arr[:])
      return

    for i in reversed(range(start, len(arr))): # iterate backwards
      arr[start], arr[i] = arr[i], arr[start] # swap
      if x == 4: print(arr) # LOG LINE
      backtrack(start + 1)

      arr[start], arr[i] = arr[i], arr[start] # undo

  backtrack(0)
  return permutations

#print(permutations(['a','b','c']))

def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int):
  
     result=[]
     def helpbacktrack(subarry,length):
        if length>=minLength:
           result.append(''.join(subarry))
        if length==maxLength:
              
           return

        for char in validCharacters:
           
           subarry.append(char)
           helpbacktrack(subarry,length+1)
           subarry.pop() 
     helpbacktrack([],0)  
     return result
print(generatePasswords(["a"], 2, 3))  

def generateAllHumanFriendlyPasswords(words: list[str], maxLength: int) -> list[str]:
    result=[]
    def backTrack(subStrings,currentLength):
       if currentLength<=maxLength and subStrings:
          result.append(' '.join(subStrings[:]))
       if currentLength==maxLength:
          return

       for word in words:  
          newlength=currentLength+len(word)+1 if subStrings else 0
          if newlength<=maxLength and word not in subStrings:
           subStrings.append(word)
           backTrack(subStrings,newlength)
           subStrings.pop()
    backTrack([],0)

    return result
print(generateAllHumanFriendlyPasswords(["apple", "dog", "zebra"], 10))     


def findwords(board,word):
   row=len(word)
   col=len(board[0])
   def backtrack(r,c,index):
      if index==len(word):
         return True
      if r<0 or r>row or c<0 or c>col or board[r][c]!=word[index]:
         return False 

      temp=board[r][c]
      board[r][c]='#'

      found=(backtrack(r+1,c,index+1)or
       backtrack(r-1,c,index+1)or 
       backtrack(r,c+1,index+1)or 
       backtrack(r,c-1,index+1)
       )   

      board[r][c]=print(found)
      return found  

   

   for i in range(row):
      for j in range(col):
         if board[i][j]==word[0] and backtrack(i,j,0):
            return True
   return False

board = [
  ['D', 'P', 'D', 'A'],
  ['A', 'V', 'O', 'G'],
  ['T', 'O', 'N', 'Y'],
  ['J', 'E', 'S', 'S']
]

print(findwords(board, "DOG"))
           


