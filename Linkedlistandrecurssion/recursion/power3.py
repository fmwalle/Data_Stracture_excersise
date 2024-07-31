def is_power_of_three(n):
    if n<1:
        return False
    while n%3==0:
        print(n)
        n//=3
    return n==1
print(is_power_of_three(12))


def is_power3_recursively(n):
    if n<1:
        return False
    if n==1:
        return True
    if n%3 != 0:
        return False
    return is_power3_recursively(n//3)
   
print(is_power3_recursively(12))        