'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

'''
#chars = ['(', ')', '{', '}', '[', ']']

def isValid ( s: str) -> bool:
    symbols = dict(('()', '[]', '{}'))
    list = []

    for item in s:
        if item in '([{':
            list.append(item)
        elif len(list) == 0 or item != symbols[list.pop()]:
            return False
    
    return len(list) == 0

response = isValid(s='{()]}')
print(response)
