def countAnagram(str)->int:
   strlist=["".join(sorted(word)) for word in str]
   uniqSet=set(strlist)

   return len(uniqSet)


print(countAnagram(["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]))
