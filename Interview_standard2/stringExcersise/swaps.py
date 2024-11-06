def swaps(list1)->list:
   if not list1:
      return []
   index=0
   seen={}
   for i ,word in enumerate(list1):
      first_char=word[0]
      if first_char in seen:
         swap_index=seen[first_char]
         list1[swap_index],list1[i]=list1[i],list1[swap_index]

         del seen[first_char]
      else:
         seen[first_char]=i   
   return list1  

print(swaps(['aOne','aTwo']))   

print(swaps(["aONE","aTWO","aTHREE","aFOUR"]))

def check_constraction(word1,word2):
   if not word1 and not word2:
      return True
   if not word1 or not word2:
      return False
   if len(word2)<len(word1):
      return False
   word1_map={}
   word2_map={}

   for chars in word1:
      word1_map[chars]=word1_map.get(chars,0)+1
   for chars in word2:
     word2_map[chars]=word2_map.get(chars,0)+1

   for keys,values in word1_map.items():
        if word2_map.get(keys,0)<values:
           return False
         
         
   return True
print(check_constraction("a", "b"))       # Output: False
print(check_constraction("aa", "ab"))     # Output: False
print(check_constraction("aa", "aab"))