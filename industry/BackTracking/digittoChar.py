def letterCombinations(digits):
    # map digit to char
    digit_to_char_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if not digits:
        return []
    result=[]
    def helperMap(current,combination):

        if len(combination)==len(digits):
            # change to string because the given was list
            result.append(''.join(combination))
            return
        charsLetter=digits[current]
        possible_letter=digit_to_char_map[charsLetter]

        for letter in possible_letter:
            combination.append(letter)

            helperMap(current+1,combination)

            combination.pop()
    helperMap(0,[])
    return result        

print(letterCombinations('23'))

def printSequ(String):

    x=0
    def helpseq(String,seq=""):
        nonlocal x
        if not String:
            x+=1
            if x==5:
                print(seq)

        helpseq(String[1:],seq+String[0])
        helpseq(String[1:],seq)
    helpseq(String)
#print(printSequ("JHON"))  

'''
You're a coder - you know how important it is to have a closing parenthesis for every opening parenthesis! Given n pairs of parentheses, write a function that generates all of the possible combinations of regular parentheses, sorted in lexicographical order.

The ordering requirement means that a sequence like "(())" will come before "()()". The both start with the same character but looking at the second character, ( is before ).

It is possible to solve the problem without sorting, but if necessary, the built in sort function can be used at the end to arrange the output in the expected order.

Example

For n = 4, the output should be

solution(n) = 
[
  "(((())))", "((()()))",
  "((())())", "((()))()", 
  "(()(()))", "(()()())", 
  "(()())()", "(())(())", 
  "(())()()", "()((()))", 
  "()(()())", "()(())()", 
  "()()(())", "()()()()"
]

'''
def generate_parentesis(n):
    result=[]
    def backtrack(current,opning,clossing):
        if len(current)==2*n:
            result.append(current)
            return
        
        if opning<n:
            backtrack(current+'(',opning+1,clossing)
        if clossing<opning:
            backtrack(current+')',opning,clossing+1)
    backtrack("",0,0)
    return result
print(generate_parentesis(4))            
class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def solution(head):
    if not head  and head.next:
        return True
    
    slow,fast=head
    
    # find the middle elemnt

    while fast and fast.next:
        slow=slow.next
        fast=fast.next
    prev=None
    #reverse the second haf
    while slow:
        temp=slow.next
        slow.next=prev
        prev=slow
        slow=temp

    # compare hafe
    firstHaf,secondHalf=head,prev
    while secondHalf :
        if firstHaf.value!=secondHalf.value:
            return False

        secondHalf=secondHalf.next
        firstHaf=firstHaf.next

    return True           

              



