def romanToInt(s):
    romanNumbersMap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    i=0
    while i<len(s):
        romanval=s[i]
        if i+1<len(s):
         
         nexRomanVal=s[i+1]
         firstVal=romanNumbersMap[romanval]
         secondVal=romanNumbersMap[nexRomanVal]
         
         if secondVal>firstVal:
            actualVal=secondVal-firstVal
            total+=actualVal
          
            i=i+2
         else:
             total+=firstVal 
             
         
             i=i+1
        else:
           total+=romanNumbersMap[romanval]
           i=i+1   
        
    return total

print(romanToInt("MCMXCIV"))        