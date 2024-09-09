
def mostFreqMistakeLength(deck: list[str]) -> int:
   
   if len(deck)<=1:
    return 0
   mistake=[]
   mistkeFrequencyMap={}
   count=1
   currentColor=deck[0]

   for i in range(1,len(deck)):
     
     if deck[i]==currentColor:
       count+=1
     else:
       if count>1:
         mistake.append(count)
       count=1
       currentColor=deck[i]
   if count>1:
     mistake.append(count)
   if not mistake:
     return 0
   for i in mistake:
     if i in mistkeFrequencyMap:
       mistkeFrequencyMap[i]+=1
     else:
       mistkeFrequencyMap[i]=1
   return max(mistkeFrequencyMap,key=mistkeFrequencyMap.get)                 

print(mostFreqMistakeLength(["R"]) == 0)
print(mostFreqMistakeLength(["B", "R"]) == 0)
print(mostFreqMistakeLength(["R", "R"]) == 2)
print(mostFreqMistakeLength(["R", "R", "B", "R", "B", "B", "R", "R", "B"]) == 2)
print(mostFreqMistakeLength(["R", "R", "R", "B", "R", "B", "R", "R", "R", "B"]) == 3)
print(mostFreqMistakeLength(["R", "R", "R", "B", "B", "R", "R", "R", "B", "B"]) == 3)
print(mostFreqMistakeLength(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B"]) == 0)
print(mostFreqMistakeLength(["R", "R", "B", "R", "R", "R", "R", "R", "B", "B"]) == 2)
print(mostFreqMistakeLength(["B", "B", "B", "B", "R", "R", "R", "B", "R", "R", "R"]) == 3)
print(mostFreqMistakeLength(["R", "R", "R", "B", "B", "B", "B", "R", "R", "R", "B"]) == 3)
print(mostFreqMistakeLength(["R", "R", "R", "B", "B", "R", "R", "R", "R", "B", "R", "B", "B", "B"]) == 3)