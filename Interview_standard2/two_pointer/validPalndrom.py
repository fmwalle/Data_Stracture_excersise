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


def validPalindrome(s):
    if not s:
        return True

    left=0
    right=len(s)-1

    while left<right:
        if s[left]!=s[right]:
            return isPalandrom(s,left+1,right) or isPalandrom(s,left,right-1)

        left+=1
        right-=1 

    return True       

  


def isPalandrom(s,left,right):
    while left<right:
        if s[left]!=s[right]:
            return False

        left+=1
        right-=1

    return True

print(validPalindrome('aaaz'))           


                 
            
