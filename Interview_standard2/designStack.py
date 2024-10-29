from collections import defaultdict
class FreqStack:
   def __init__(self):
     self.freq=defaultdict(int)

     self.group=defaultdict(list)

     self.maxfreq=0
   def push(self,value):
      self.freq[value]+=1
      
      if self.freq[value]>self.maxfreq:
         self.maxfreq=self.freq[value]

      self.group[self.freq[value]].append(value)

   def pop(self):

      vals=self.group[self.maxfreq].pop()
      self.freq[vals]-=1
      if not self.group[self.maxfreq]:
         self.maxfreq-=1

      return vals    

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
