def canMatchFellows(skillMap: dict) -> bool:
    if len(skillMap)==0:
        return True
    if len(skillMap)%2!=0:
        return False
    skilSet=set()

    for skill in skillMap.values():
        if skill in skilSet:
            skilSet.discard(skill)
        else:
            skilSet.add(skill)
    return len(skilSet)==0           

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == False)
skillMap = {"oliver": 3, "pixel": 3, "pinky": 3}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, "paavo" : 1}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3, "tobey": 3}
print(canMatchFellows(skillMap) == True)

print(canMatchFellows({"oliver": 1}) == False)

print(canMatchFellows({}) == True)
