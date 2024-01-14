def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for val in tokens:
        if val in "+-*/":
            second = stack.pop()
            first = stack.pop()

            if val == "+":
                result = first + second
                stack.append(result)
            elif val == "-":
                result = first-second
                stack.append(result)
            elif val == "*":
                result = first*second
                stack.append(result)
            elif val == "/":
                result = int(first/second)
                stack.append(result)
        else:
            stack.append(int(val))
        print(stack[-1])
    return stack.pop()