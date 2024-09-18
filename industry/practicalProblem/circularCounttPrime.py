import math
def countCircularPrimes(upperBound: int):
  if upperBound<=1:
    return 0
  countCircularPrime=set()
  if upperBound >2:
      countCircularPrime.add(2)
  
  for i in range(3,upperBound):
     if not isPrime(i):
       continue
     else:
      rotations = roundingNum(i)
      if all(isPrime(rot) for rot in rotations):
                countCircularPrime.update(rotations)

  return len(countCircularPrime)


def isPrime(n):
  if n<=1:
    return False
  
  for i in range(2,int(math.sqrt(n))+1):

    if n %i==0:
      return False
  return True

def roundingNum(primeNum):

  rotation=[]
  Chnage_primeNumber_str=str(primeNum)
  for i in range(len(Chnage_primeNumber_str)):
     rot=int(Chnage_primeNumber_str[i:]+Chnage_primeNumber_str[:i])
     rotation.append(rot)
  
  return rotation

print(roundingNum(179))
print(countCircularPrimes(990))  
