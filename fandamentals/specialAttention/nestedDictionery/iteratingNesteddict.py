import statistics


data = [{"oliver": 2, "pixel": 1, "pinky": 4}, 
        {"michael": 2, "oliver": 3, "pinky": 3},
        {"michael": 1, "oliver": 1, "pixel": 1}]
  
def collectDatainOnePlace(fellowdata):
    storeinone = {}  
    for entry in fellowdata:
        for fellow, rating in entry.items():
            if fellow not in storeinone:
                storeinone[fellow] = {'session': 0, 'rating': 0, 'ratings_list': []}
            storeinone[fellow]['session'] += 1
            storeinone[fellow]['rating'] += rating
            storeinone[fellow]['ratings_list'].append(rating)
    print(storeinone)        
    return storeinone

def highestAveragefellow(fellowdata) -> str:
    storeinone = collectDatainOnePlace(fellowdata)
    highest = float('-inf')
    bestFellow = ''
    for fellow, values in storeinone.items():
        avg_rating = values['rating'] / values['session']
        if avg_rating > highest:
            highest = avg_rating
            bestFellow = fellow
    return bestFellow

def lowestAverageRating(fellowdata) -> str:
    storeinone = collectDatainOnePlace(fellowdata)
    lowest = float('inf')
    weakestFellow = ''
    for fellow, values in storeinone.items():
        avg_rating = values['rating'] / values['session']
        if avg_rating < lowest:
            lowest = avg_rating
            weakestFellow = fellow
    return weakestFellow

def mostNumberofSession(fellowdata) -> str:
    storeinone = collectDatainOnePlace(fellowdata)
    highestSession = float('-inf')
    mostAttendat = ''
    for fellow, values in storeinone.items():
        if values['session'] > highestSession:
            highestSession = values['session']
            mostAttendat = fellow
    return mostAttendat


def mostConsistentRating(fellowdata) -> str:
    storeinone = collectDatainOnePlace(fellowdata)
    lowestStdDev = float('inf')
    mostConsistentFellow = ''

    for fellow, values in storeinone.items():
        if len(values['ratings_list']) > 1:
            std_dev = statistics.stdev(values['ratings_list'])
        else:
            std_dev = 0  
        
        if std_dev < lowestStdDev:
            lowestStdDev = std_dev
            mostConsistentFellow = fellow

    return mostConsistentFellow

print(collectDatainOnePlace(data))
#print(highestAveragefellow(data))
#print( lowestAverageRating(data))
#print(mostNumberofSession(data))
#print( mostConsistentRating(data))
