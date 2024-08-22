def count7(num):
    def helper(num):
        if num==0:
            return 0
        count=1 if num%10==7 else 0
        
        count+helper(num//10)  
    return helper(num)       

def findMinIndex(array):
    def findHelper(array,index):
        if index==len(array):
            return -1
        min_index=findHelper(array,index+1)

        if min_index == -1 or array[index] < array[min_index]:
            return index
        else:
            return min_index
    
    if not array:
        return -1
    return findHelper(array, 0)
def changeHexadecimal(str)->int:
    if len(str)==0:
        return 0
    
    hex_digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }


    # checking each index
    sum=0
    for chars in str:
        sum*=16
        if chars in hex_digits:
            sum+=hex_digits[chars]
        else:
            raise "error"   
    return sum     

print(changeHexadecimal('2694'))