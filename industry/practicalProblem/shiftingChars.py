def shift_chars(s: str) -> str:
    if not s:
        return ""
    returnStr=[]
    for chars in s:
        if chars.isalpha():
           baseChars=ord('a') if chars.islower() else ord('A')
           shiftedChars= chr(baseChars+(ord(chars)-baseChars+1)%26)
           returnStr.append(shiftedChars)
        else:
            returnStr.append(chars)
    return ''.join(returnStr)      

print(shift_chars('b c'))     