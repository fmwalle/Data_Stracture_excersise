def strStr(given: str, target: str) -> int:
    if not str :
        return -1
    
    return given.find(target)
def find_first_occurrence_manual(string, target):
    for i in range(len(string)-len(target)+1):
        if string[i:i+len(target)]==target:
            return i
    return -1    
print(find_first_occurrence_manual('Hello','llp'))