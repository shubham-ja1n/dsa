def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    
    for char in s:
        if char in ['{', '[', '(']:
            stack.append(char)
            continue
        if len(stack)==0:
            return False
        value = stack.pop()
        if char == '}' and value != '{':
            return False
        if char == ']' and value != '[':
            return False
        if char == ')' and value != '(':
            return False
    if len(stack) > 0:
        return False
    else:
        return True