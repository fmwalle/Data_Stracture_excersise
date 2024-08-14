def sumNestedList(array:list[int])->int:
    def helpsum(array,index,sum):
        if index>=len(array):
           return sum
        

        return helpsum(array,index+1,sum+array[index])
    return helpsum(array, 0, 0)
    

print(sumNestedList([1,2,3]))

def sumNested(array):
    def helperSum(array):
        totalsum=0
        for elemnt in array:
            if isinstance 

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

def sumNestedListWithDepth(array):
    total_sum = 0
    stack = [(array, 1)]  # Each element in stack is a tuple (list, depth)
    
    while stack:
        current, depth = stack.pop()
        current_sum = 0
        for element in current:
            if isinstance(element, list):
                stack.append((element, depth + 1))
            else:
                current_sum += element
        
        total_sum += current_sum * depth
    
    return total_sum

# Example usage
print(sumNestedListWithDepth([4, [2, 3]]))  # Output: 14
print(sumNestedListWithDepth([4, [2, [3]]]))  # Output: 26

# Example usage
print(sumNestedList([1, 2, 3]))  # Output: 6
print(sumNestedList([1, [1, 2, 3], 3]))  # Output: 10
print(sumNestedList([1, [1, [1, [1, [1]]]]]))  # Output: 5

        

