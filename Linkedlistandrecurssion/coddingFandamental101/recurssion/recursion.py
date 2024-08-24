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

def count_sum_eight(nums):
    sum=0
    count=0
    while nums>0:
        if nums%10==8:
            count+=1
            sum+=count
        elif nums%10!=8:
            count-=1
            sum+=count
        nums=nums//10
    return sum 

#print(count_sum_eight(8818))    
def count_Eight_recursive(nums):
       def helper8(nums):
        if nums == 0:
            return 0
        if nums % 10 == 8:
           if (nums//10)%10==8:
               return 2+helper8(nums//10)
           else:
               return 1+helper8(nums//10)
        else:
            return helper8(nums // 10)  # Added return here

       return helper8(nums)   
    
print(count_Eight_recursive(8818))    

def nonsense(a,b):
   
    if a==b:
        return 5
    c=nonsense(a+1,b-1)+a+b
    print(c)
    return c 
print(nonsense(3,9))

def runi(a,b):
    if len(a)>=b:
        return "Ith"
    a=a+runi(a,b-1)+"ber"
    print(a)
    return a
print(runi("jah",6))
