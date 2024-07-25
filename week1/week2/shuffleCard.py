def faro(deck: list[str]) -> list[str]:
    mid=len(deck)//2
    afterShuffle=[]
    topHalf=deck[:mid]
    bottomHalf=deck[mid:]

    for tchar,bchar in zip(topHalf,bottomHalf):
        afterShuffle.append(tchar)
        afterShuffle.append(bchar)
    return afterShuffle

newDeckOrder = [
  'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
  'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
  'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C', 'AC',
  'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AH']

#firstFaro = faro(newDeckOrder)   
#print(firstFaro) 

def faroSolution2(deck:list[str]):
    mid=len(deck)//2
    topHalf=deck[:mid]
    botomHalf=deck[mid:]
    shufled=[]

    for i in range(mid):
        shufled.append(topHalf[i])
        shufled.append(botomHalf[i])
    return shufled 
newDeckOrder = [
  'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
  'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
  'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C', 'AC',
  'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H', 'AH']

firstFaro = faroSolution2(newDeckOrder)   
print(firstFaro)



















































































































  





















