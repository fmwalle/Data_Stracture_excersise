def quick_sort(array,low,high):
    if low<high:
        pivot_index=partion(array,low,high)

        quick_sort(array,low,pivot_index-1)
        quick_sort(array,pivot_index+1,high)
    return array  


def partion(array,low,high):

    i=low-1
    pivot=array[high]

    for j in range(low,high):
        if array[j]<=pivot:
            i+=1

            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1        
array = [10, 7, 8, 9, 1, 5]
print(quick_sort([10,7,8,8,1,5],0,len(array)-1))