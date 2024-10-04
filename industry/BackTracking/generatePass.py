from itertools import product
# product is a tool used to generate combination based on given length
def generatePasswords(chars, minLen, maxLen):
    result=[]
    for length in range(minLen,maxLen+1):
        for password in product(chars,repeat=length):
            result.append(''.join(password))
    return result
#print(generatePasswords(["a", "b", "c"], 2, 3))


def is_interleaving(x: str, y: str, s: str) -> bool:
    
    if len(x)+len(y)!=len(s):
        return False
    mapping_Input_x_y={}
    mapping_output_s={}

    for chars in x:
        if chars in  mapping_Input_x_y:
            mapping_Input_x_y[chars]+=1
        else:
            mapping_Input_x_y[chars]=1
    for charsy in y:
         if charsy in y in mapping_Input_x_y:
            mapping_Input_x_y[charsy]+=1
         else:
            mapping_Input_x_y[charsy]=1  
    for charsout in s:
        if charsout in mapping_output_s:
            mapping_output_s[charsout]+=1
        else:
            mapping_output_s[charsout]=1  
    for value,key in mapping_output_s.items():
        if value not in mapping_Input_x_y:
            return False
        elif mapping_Input_x_y[value]!=key:
            return False
    return True                        
print(is_interleaving("AABCC", "DBBCA", "AADBBCBCAC") == True)
print(is_interleaving("ABC", "BCD", "BABCCD") == True)
print(is_interleaving("ABC", "BCD", "ABCBCD") == True)
print(is_interleaving("ABC", "BCD", "BCDABC") == True)
print(is_interleaving("ABC", "BCD", "BCABDC") == True)
print(is_interleaving("ABC", "BCD", "BABCDD") == False)
print(is_interleaving("ABC", "BCD", "ABBCCD") == True)
print(is_interleaving("ABC", "BCD", "DCCBBA") == False)