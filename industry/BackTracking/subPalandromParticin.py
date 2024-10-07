def subPalndrom(string):
    result=[]

    def backtrackString(paladrom_array,start):
        if start==len(string):
             result.append(paladrom_array[:])
             return

        for i in range(start,len(string)):
             substring=string[start:i+1]  

             if palandrom(substring):
                  paladrom_array.append(substring)
                  backtrackString(paladrom_array,i+1)
                  paladrom_array.pop()

        

    backtrackString([],0)
    return result    
def palandrom(substring):
        
        return substring==substring[::-1]

       
print(palandrom("abbac"))

print(subPalndrom('aab'))


def printSeq(string):
     x=0
     def helper(string,sequ=""):
        nonlocal x
        if not string:
               x+=1
               if x==5:
                    print(sequ)
                    return
        helper(string[1:],sequ+string[0])  
        helper(string[1:],sequ)   
     helper(string,"")
     return x

print(printSeq("JOHN"))