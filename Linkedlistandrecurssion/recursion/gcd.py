def findGcd_iterative(n:int,m:int):
    common=min(n,m)
    gcd=float('-inf')

    for i in range(1,common+1):

        if n%i==0 and m%i==0:
            gcd=i
    return gcd
def findGcd_recursively(n:int,m:int,index:int=1,gcd=1):
     
    if index>min(n,m):
        return gcd
    if n%index==0 and m%index==0:
        gcd=index
    return findGcd_recursively(n,m,index+1,gcd)    
print(findGcd_recursively(27,9))            

