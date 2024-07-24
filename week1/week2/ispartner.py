def hasRepeatTangoPartner(firstSession: list[list[str]], secondSession: list[list[str]]):

    firstDic={":".join(sorted(item))for item in firstSession}


    for vales in secondSession:
        seconDic=":".join(sorted(vales))
        if seconDic in firstDic:
            return True

    return False 
# solution2
def hasRepeatTangoPartner2(firstSession: list[list[str]], secondSession: list[list[str]]):
    firstTango=dict()

    for item1,item2 in firstSession:
        firstTango[item1]=item2
    for item1,item2 in secondSession:
        if item1 in firstTango and firstTango[item1]==item2 or item2 in firstTango and firstTango[item2]==item1:
            return True     
    return False

session1 = [["Alice", "Baxter"]]
session2 = [["Baxter", "Alice"]]
#True
print(hasRepeatTangoPartner2(session1, session2))

# disjoint list false
session1 = [["Alice", "Baxter"]]
session2 = [["Charles", "Davis"]]
print(hasRepeatTangoPartner2(session1, session2))

# partner mixing=false
session1 = [["Alice", "Baxter"], ["Charles", "Davis"]]
session2 = [["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner2(session1, session2) )

# more partner mixing false
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Charles"], ["Baxter", "Davis"], ["Alice", "Daniels"]]
print(hasRepeatTangoPartner2(session1, session2))

# 1 overlap TRUE
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jack", "Daniels"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2))

# overlap with flipped partners True
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Daniels", "Jack"], ["Alice", "Charles"], ["Baxter", "Davis"]]
print(hasRepeatTangoPartner(session1, session2))

# no overlap False
session1 = [["Alice", "Baxter"], ["Charles", "Davis"], ["Jack", "Daniels"]]
session2 = [["Jono", "Paavo"], ["Zoe", "Angus"], ["Oliver", "Pixel"]]
print(hasRepeatTangoPartner(session1, session2) )  