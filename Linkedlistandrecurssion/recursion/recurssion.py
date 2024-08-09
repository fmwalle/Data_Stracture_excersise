import math
def factorial(n)->int:
    if n<0:
        return -1
    elif n<2:
        return 1
    factor=1
    for i in range(1,n+1):
       factor*=i
    return factor

def recursively(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else :
        return n*recursively(n-1)
print(recursively(5)) 


def exponential(n,k):
    def helpExponent(n,current,count):
        if current>n:
            return -1
        if current==n:
            return count
      
        return helpExponent(n,current*k,count+1)
    return helpExponent(n,k,1)  
print(exponential(9,3)) 


print("int")
print(int(-3 / 2))
print("floor")
print(math.floor(3 /2))
print("ceil")
print(math.ceil(3 / 2))
print("sqrt")
print(math.sqrt(2))
print("pow")
print(math.pow(2, 3))


   

    