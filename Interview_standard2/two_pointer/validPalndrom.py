def isPalindrome(s):
    if not s:
        return False
    
    j=len(s)-1
    i=0
    while i<=j:
        if not s[i].isalnum() :
            i+=1
        elif not s[j].isalnum():
            j-=1
        else:
            if s[i].lower()!=s[j].lower():
                return False

            i+=1
            j-=1

    return True                

print(isPalindrome('A man, a plan, a canal: Panama'))        
                 
            
