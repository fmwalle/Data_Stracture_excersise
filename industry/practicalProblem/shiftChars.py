def shift_chars(s: str) -> str:
    if not s:
        return ""
    newStr=[]
    for chars in s:
        if chars.isalpha():
            base=ord('a') if chars.islower() else ord('A')
            shifted_Char=chr(base+(ord(chars)-base+1)%26)
            newStr.append(shifted_Char)
        else:
            newStr.append(chars) 
    return ''.join(newStr)           

print(shift_chars("the quick brown fox"))       
