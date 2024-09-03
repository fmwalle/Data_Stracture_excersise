def earliestFellows(fellowTimes: dict):
    smallest=float('inf')
    listofName=[]
    for name,days in fellowTimes.items():
       if days< smallest:
           listofName=[name]
           smallest=days
       elif smallest==days:
           listofName.append(name)   
           
          

    return listofName           
fellowTimes = {"oliver": 3}
# == ["oliver"]
print(earliestFellows(fellowTimes))

#== ["oliver", "tobey"]
fellowTimes = {"oliver": 3, "tobey": 3}
print(earliestFellows(fellowTimes) )
#== ["tobey"]
fellowTimes = {"oliver": 3, "pinky": 4, "pixel": 2, "tobey": 1}
print(earliestFellows(fellowTimes) )
# == ["pinky", "tobey"]
fellowTimes = {"oliver": 3, "pinky": 1, "pixel": 2, "tobey": 1}
print(earliestFellows(fellowTimes))
#== ["jess", "zoe", "jono"]
fellowTimes = {"tony": 3, "jess": 1, "paavo": 2, 
"zoe": 1, "ariel": 2, "jono": 1, "angus": 3}
print(earliestFellows(fellowTimes) )               