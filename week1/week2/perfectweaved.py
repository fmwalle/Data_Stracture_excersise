def isPerfectWeave(deck: list[str]) -> bool:
    for i in range(1,len(deck)):
        if deck[i-1]==deck[i]:
            return False
    return True

def isPerfectWeave2(deck: list[str]) -> bool:
    myDict={}
    for char in deck:
        myDict[char]=myDict.get(char,1)+1
     
        value=myDict.get(char)
    for vals in myDict.values():
        if vals!=value:
            return False
    return True    

print(isPerfectWeave2(["R", "R", "R", "R", "R"]))
print(isPerfectWeave2(["R", "B", "R", "R", "R"]))
print(isPerfectWeave2(["B", "B", "R", "B", "R"]) )
print(isPerfectWeave2(["R", "B", "R", "B", "B"]))
print(isPerfectWeave2(["B", "R", "B", "R", "B", "R", "B", "R", "B", "R"]))
print(isPerfectWeave2(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B"]))   