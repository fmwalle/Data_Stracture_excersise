def shift_chars(s: str):
    if not s:
        return ""
    shiftedStr=[]
    for chars in s:
        if chars.isalpha():

            baseChar= 'a' if chars.islower()  else 'A'
            numberedBase=ord(baseChar)
            shiftedChar=numberedBase+(ord(chars)-numberedBase+1)%26
            shiftedStr.append(chr(shiftedChar))
        else:
           shiftedStr.append(chars)

    return ''.join(shiftedStr)

print(shift_chars("A b"))       
def maxProfitPotential(prices: list[float]) -> float:

    minimumBuy=float('inf')
    maxProfit=0

    for sell in prices:
        profit=sell-minimumBuy
        minimumBuy=min(sell,minimumBuy)
        maxProfit=max(maxProfit,profit)