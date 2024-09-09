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