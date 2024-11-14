def sieveOfEratosthenes(upperBound: int) -> set[int]:
    answer=set()
    if upperBound<2:
        return answer
    answer.add(2)
    for i in range(3,upperBound+1,1):
        n=2
        answer.add(i)
        while n<i:
           if i%n==0:
               answer.remove(i)
               break
           n+=1
    return answer
print(sieveOfEratosthenes(2))
print(sieveOfEratosthenes(3))
print(sieveOfEratosthenes(4))
print(sieveOfEratosthenes(5))
print(sieveOfEratosthenes(6))
print(sieveOfEratosthenes(10))
print(sieveOfEratosthenes(99))
#print(sieveOfEratosthenes(1000))      