def theFirstRepeted(words:str)->chr:
    setofChars=set()

    for char in words:
        if char in setofChars:
            return char
        else:
            setofChars.add(char)
    return "_"   

print(theFirstRepeted("Fikir"))     
