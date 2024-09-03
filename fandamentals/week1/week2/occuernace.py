
def printNameFreq(names: str) -> str:
    if not names:
        return "No body appeared"
    
    # Split and strip names to remove any leading/trailing whitespace
    array_of_names = [name.strip() for name in names.split(",")]

    # Create a dictionary to count occurrences
    name_dict = {}
    for name in array_of_names:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    
    # Create the result string list
    result = []
    for name in name_dict:
        times = name_dict[name]
     
        result.append(f"{name} appeared {times} times.")
    
    # Join the result list into a single string with newline characters
   # return "\n".join(result)

#print(printNameFreq("Tony, Jessica, Paavo, Zoe, Tony, Jessica, Tony") ) 

def printNameFreq2(names: str):
    if not names:
        return "it doesn't appered"
    split_names = names.split(", ")
    nameDict={}
    for name in split_names:
        nameDict[name]=nameDict.get(name,0)+1

    result=[]
    for name,frequency in nameDict.items():
       result.append(f"{name} appeared {frequency} time{'s' if frequency > 1 else ''}.")
    return "\n".join(result)   

print(printNameFreq2("Tony, Jessica, Paavo, Zoe, Tony, Jessica, Tony") ) 