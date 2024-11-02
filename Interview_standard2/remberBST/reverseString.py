def reverseWord(s: str) -> str:
    if not str:
        return ""
    result=s[::-1]
    return result.strip()

print(reverseWord("Fikir"))

def reverseWords(s:str)->str:
    if not str:
        return ""
    
    words=[word  for word in s.split(" ") if word]
    return ' '.join(words[::-1])        

print(reverseWords('the sky is blue ')) 
print(reverseWords(' hello world ')) 
