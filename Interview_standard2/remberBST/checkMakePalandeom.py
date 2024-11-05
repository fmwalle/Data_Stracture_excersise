def is_make_palandrom(word:str):
    if not word:
        return True
    
    word_Map={}

    for chars in word:
        if chars in word_Map:
            word_Map[chars]+=1

        else:
            word_Map[chars]=1
    od_count=0
    for value in word_Map.values():
        if value%2!=0:
            od_count+=1
        
    return od_count<=1

print(is_make_palandrom("aac"))    
