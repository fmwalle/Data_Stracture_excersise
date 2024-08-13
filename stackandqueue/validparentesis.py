def validparentesis(s)->bool:
    stack=[]
    mapping={"}":"{",")":"(","]":"["}
    for char in s:
        if char in mapping:
            openparentsis=mapping[char]
            if stack and stack[-1]!=openparentsis:
                return False
            stack.pop()
        else:
            stack.append(char)

       
    return True if not stack else False
def removeOuterMostParentesis(s):
    popen,result=0,[]

    for chars in s:
        if chars==')':
         popen-=1 
        if popen>0:
            result.append(chars)
        if chars=='(':
            popen+=1
    return "".join(result)                           

print(removeOuterMostParentesis("(()())(())(()(()))") )            