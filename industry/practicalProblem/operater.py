def check_arithmetic_expressions(operand1,operator,operand2,result):
    if not (len(operand1) == len(operator) == len(operand2) == len(result)):
        return False
    expected=[]
    for i in range(0,len(operand1)):
        val1=operand1[i]
        val2=operand2[i]
        if operator[i]=='+':
            res=val1+val2
        elif operator[i]=='-':
           res=val1-val2
        elif operator[i]=='*':
           res=val1*val2
        elif operator[i]=='/':
           if operand2[i]==0:
               expected.append(False)
           else:
               res=val1//val2
                  
        else:
            expected.append(False)
        expected.append(res==result[i])    
    return expected   
operands1 = [3, 5, 2, 9]
operators = ['+', '-', '*', '/']
operands2 = [2, 3, 4, 3]
results = [5, 2, 8, 3]
print(check_arithmetic_expressions(operands1, operators, operands2, results))  # Output: [True, True, True, True]                

operands1 = [3, 5, 2, 9]
operators = ['+', '-', '*', '/']
operands2 = [2, 3, 4, 3]
results = [6, 1, 7, 4]
print(check_arithmetic_expressions(operands1, operators, operands2, results))  # Output: [False, False, False, False]