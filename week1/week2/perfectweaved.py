def isPerfectWeave(deck: list[str]) -> bool:
    for i in range(1,len(deck)):
        if deck[i-1]==deck[i]:
            return False
    return True
print(isPerfectWeave(["R", "R", "R", "R", "R"]))
print(isPerfectWeave(["R", "B", "R", "R", "R"]))
print(isPerfectWeave(["B", "B", "R", "B", "R"]) )
print(isPerfectWeave(["R", "B", "R", "B", "B"]))
print(isPerfectWeave(["B", "R", "B", "R", "B", "R", "B", "R", "B", "R"]))
print(isPerfectWeave(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B"]))   