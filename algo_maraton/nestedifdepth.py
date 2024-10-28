def vbNesting(controlFlow: list[str]) -> int:

    if not controlFlow or not controlFlow[0] =='if':
        return -1
    
    stack_depth=0
    depth=0
    max_depth=0
    prev=None

    for keys in controlFlow:
        if keys=='if':
            depth+=1
            max_depth=max(max_depth,depth)
            stack_depth+=1

        elif keys=='endif':
            if stack_depth==0:
                return -1
            depth-=1
            stack_depth-=1

        elif keys=='else':
            if prev=="else":
                return -1
            if prev=='endif' or prev==None:
                return -1
        elif keys == 'elseif':
            if prev == 'else':
                return -1  # 'elseif' cannot follow 'else'
            if prev in (None, 'endif'):
                return -1  
        else:
            return -1
        
        prev=keys
    if stack_depth!=0:
        return-1
    return max_depth

print(vbNesting(["if"]))  # Expected: -1
print(vbNesting(["endif"]))  # Expected: -1
print(vbNesting(["if", "endif"]))  # Expected: 1
print(vbNesting(["if", "else", "endif"]))  # Expected: 1
print(vbNesting(["if", "endif", "if", "endif"]))  # Expected: 1
print(vbNesting(["if", "if", "endif", "endif"]))  # Expected: 2
print(vbNesting(["if", "if", "if", "endif", "endif", "endif"]))  # Expected: 3
print(vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]))            
                    























