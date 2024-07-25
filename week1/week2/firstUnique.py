def firstUniqChar(self):
       
        listStr=list(self)
        charDict={}
        for char in listStr:
         if char in charDict:
            charDict[char]=charDict.get(char)+1
         else:
            charDict[char]=1

        for chars,vals in charDict.items():
            if vals==1:
                index=listStr.index(chars)
                return index
        return -1 

print(firstUniqChar("leetcode"))   

def firstUniqChar2(s):

     for i in s:
            if s.rindex(i)==s.index(i):
                return s.index(i)
    
     return -1
print(firstUniqChar2("leetcode")) 