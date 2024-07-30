def everyXth(arr: list[int], x: int) -> list[int]:

    everyx=[]
    for num in arr:
        if num%x==0:
            everyx.append(num)
    return everyx

print(everyXth([], 1000) )
print(everyXth([5], 1) )
print(everyXth([5], 2) )
print(everyXth([1,2,3,4,5,6], 2) )
print(everyXth([1,2,3,4,5,6], 3) )
print(everyXth([1,2,3,4,10,6], 5) )
print(everyXth([1,2,3,4,10,6], 8) )        