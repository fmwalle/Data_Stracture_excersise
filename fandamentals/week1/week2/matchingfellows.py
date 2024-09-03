def canMatchFellows(skillMap: dict) -> bool:
    setoflevels=set()

    for levelSkill in skillMap.values():
        if levelSkill not in setoflevels:
            setoflevels.add(levelSkill)
        else:
            setoflevels.remove(levelSkill)   
       
    return len(setoflevels)==0


skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) )

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) )

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3}
print(canMatchFellows(skillMap) )

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, "paavo" : 1}
print(canMatchFellows(skillMap) )

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3, "tobey": 3}
print(canMatchFellows(skillMap) )

print(canMatchFellows({"oliver": 1}) )

print(canMatchFellows({}) )