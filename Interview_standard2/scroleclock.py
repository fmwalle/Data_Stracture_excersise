def minScrollToSet(oldTime: str, newTime: str) -> int:
    old_hours=oldTime.split(":")
    new_hours=newTime.split(":")
    hr1=int(old_hours[0])
   
    hr2=int(new_hours[0])
   
    min1=int(old_hours[1])
    min2=int(new_hours[1])
    
    hourshift_up=(hr1-hr2)%24
    hour_shift_doun=(hr2-hr1)%24
    min_hour=min(hour_shift_doun,hourshift_up)

    mini_shift_up=(min1-min2)%60
    min_shift_down=(min2-min1)%60
    min_min=min(min_shift_down,mini_shift_up)

  

    return min_hour+min_min
print(minScrollToSet("7:30", "8:00") == 31)
print(minScrollToSet("7:00", "6:31"))
print(minScrollToSet("7:00", "6:25") == 26)
print( minScrollToSet("7:00", "6:31") == 30)
assert minScrollToSet("7:00", "6:25") == 26
assert minScrollToSet("7:30", "8:00") == 31
assert minScrollToSet("7:00", "8:00") == 1
assert minScrollToSet("8:00", "8:00") == 0
assert minScrollToSet("6:59", "7:01") == 3
assert minScrollToSet("22:00", "2:00") == 4
assert minScrollToSet("12:00", "00:00") == 12
assert minScrollToSet("23:59", "00:00") == 2

