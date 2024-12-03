def maxProfit(prices):
    left=0
    right=1
    max_profit=0

    while right<len(prices):
        if prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)

        else:
            left=right

        right+=1
    return max_profit

print(maxProfit([7,1,5,3,6,4]))            


def lengthOfLongestSubstring(s):

    left=0
    max_height=0
    char_set=set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_height=max(max_height,right-left+1)
    return max_height

print(lengthOfLongestSubstring('abcabcbb'))        
