def reverseWord(s: str) -> str:
    if not str:
        return ""
    result=s[::-1]
    return result.strip()

print(reverseWord("Fikir"))


