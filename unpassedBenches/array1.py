
def countOccurance(charStr:str)->list[chr]:
    listStr=list(charStr)
    charDict={}

    sortedarr=[]

    for chars in listStr:
         charDict[chars]=charDict.get(chars,0)+1
             
    sortedarr = sorted(charDict.keys(), key=charDict.get, reverse=True)

    return sortedarr

print(countOccurance("gggghhleee"))
                