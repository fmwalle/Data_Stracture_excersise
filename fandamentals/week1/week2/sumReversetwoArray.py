def sumInReverse(arr1: list[int], arr2: list[int]) -> list[int]:
    sumArray=[]
    j=len(arr2)
    i=0
    while i< len(arr1) and j>0:

        sum=arr1[i]+arr2[j-1]
        sumArray.append(sum)
        i+=1
        j-=1
    return sumArray


print(sumInReverse([], []))
print(sumInReverse([5], [7]) )
print(sumInReverse([1,2,3], [10,20,30]) )
print(sumInReverse([1,2,3,4], [40,30,20,10]))