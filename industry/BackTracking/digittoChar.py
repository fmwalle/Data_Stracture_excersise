def letterCombinations(digits):
    # map digit to char
    digit_to_char_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if not digits:
        return []
    result=[]
    def helperMap(current,combination):

        if len(combination)==len(digits):
            result.append(''.join(combination))
            return
        charsLetter=digits[current]
        possible_letter=digit_to_char_map[charsLetter]

        for letter in possible_letter:
            combination.append(letter)

            helperMap(current+1,combination)

            combination.pop()
    helperMap(0,[])
    return result        

print(letterCombinations('23'))

def printSequ(String):

    x=0
    def helpseq(String,seq=""):
        nonlocal x
        if not String:
            x+=1
            if x==5:
                print(seq)

        helpseq(String[1:],seq+String[0])
        helpseq(String[1:],seq)
    helpseq(String)
print(printSequ("JHON"))              

              



