def sumNestedList(array:list[int])->int:
    def helpsum(array,index,sum):
        if index>=len(array):
           return sum
        

        return helpsum(array,index+1,sum+array[index])
    return helpsum(array, 0, 0)
    

print(sumNestedList([1,2,3]))



def sumNestedList(array):
    total_sum = 0
    stack = [array]
    
    while stack:
        current = stack.pop()
        for element in current:
            if isinstance(element, list):
                stack.append(element)
            else:
                total_sum += element
    
    return total_sum

# Example usage
print(sumNestedList([1, 2, 3]))  # Output: 6
print(sumNestedList([1, [1, 2, 3], 3]))  # Output: 10
print(sumNestedList([1, [1, [1, [1, [1]]]]]))  # Output: 5

        

