from collections import defaultdict
class FreqStack:
 def __init__(self):
   self.frquenc_map=defaultdict(int)
   self.grouping=defaultdict(list)

   self.max_frquency=0

 def push(self,value):
   self.frquenc_map[value]+=1

   if self.frquenc_map[value]>self.max_frquency:
      self.max_frquency=self.frquenc_map[value]

   self.grouping[self.frquenc_map[value]].append(value)
 def pop(self):

   max_val=self.grouping[self.max_frquency].pop()

   self.frquenc_map[max_val]-=1

   if not self.grouping[self.max_frquency]:
      self.max_frquency-=1

   return max_val



freqStack = FreqStack()
freqStack.push(5)  # Stack: [5]
freqStack.push(7)  # Stack: [5, 7]
freqStack.push(5)  # Stack: [5, 7, 5]
freqStack.push(7)  # Stack: [5, 7, 5, 7]
freqStack.push(4)  # Stack: [5, 7, 5, 7, 4]
freqStack.push(5)  # Stack: [5, 7, 5, 7, 4, 5]

print(freqStack.pop())  # Returns 5, as 5 is most frequent. Stack: [5, 7, 5, 7, 4]
print(freqStack.pop())  # Returns 7, since 5 and 7 are most frequent, but 7 is closer to top. Stack: [5, 7, 5, 4]
print(freqStack.pop())  # Returns 5, as 5 is now the most frequent. Stack: [5, 7, 4]
print(freqStack.pop())  # Returns 4. Stack: [5, 7]
