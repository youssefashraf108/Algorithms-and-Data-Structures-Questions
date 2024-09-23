"""Q5) Given a string s, containing just characters '({[' and '}])'. determine if the inout string is valid
open brackets must be closed by same type of brackets
open brackets must be closed in correct order """

def isValid(s):
    stack = []
    for char in s:
        if char in '{([':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                if \
                    (char == '}' and stack[-1] == '{' or \
                     char == ')' and stack[-1] == '(' or \
                        char == ']' and stack[-1] == '['):
                   stack.pop()                   
    return not stack
                

        


s = "}{()}"
if isValid(s):
    print("Valid String")
else:
    print("Not Valid String")