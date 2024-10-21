def addStars(word: str) -> str:
  def helper(word,result,index):
    if index==len(word)-1:
       result.append(word[index])
       return ''.join(result)
    
    result.append(word[index])
    result.append('*')
    return helper(word,result,index+1)
  return helper(word,[],0) 

print(addStars("ab"))


def sumDigits(n: int) -> int:
  
  sum=0
  while n>0:
   
   sum+=n%10
   n=n//10
  return sum
print(sumDigits(126) == 9)
print(sumDigits(49) == 13)
print(sumDigits(12) == 3)
print(sumDigits(10) == 1)
print(sumDigits(1) == 1)
print(sumDigits(0) == 0)
print(sumDigits(730) == 10)
print(sumDigits(1111) == 4)
print(sumDigits(11111) == 5)
print(sumDigits(10110) == 3)
print(sumDigits(235) == 10)
  
