def findRepeatedDnaSequences(s):
 
 seen=set()
 repeted=set()

 for i in range(len(s)-9):
  
  sequence=s[i:i+10]
  print(sequence)

  if sequence in seen:
   repeted.add(sequence)
  else:
   seen.add(sequence)
 return list(repeted)  

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) 

def minScrollToSet(oldTime: str, newTime: str) -> int:
 
   oldHour, oldMin=map(int,oldTime.split(":"))
   newHour, newMin=map(int,newTime.split(":"))

   minHour=abs(oldHour-newHour)
   hourmoves=min(minHour,24-minHour)
   minMin=abs(oldMin-newMin)
   minMoves=min(minMin,60-minMin)

   return minMoves+hourmoves
  
print(minScrollToSet("8:24","4:50"))
print(minScrollToSet("7:00", "6:31") == 30)
print(minScrollToSet("7:00", "6:25") == 26)
assert minScrollToSet("7:30", "8:00") == 31