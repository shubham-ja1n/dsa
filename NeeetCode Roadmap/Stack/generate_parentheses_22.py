def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    stack = []


    def backtrack(openN, closedN):

        if openN == closedN == n:
            s = "".join(stack)
            res.append(s)
        
        if openN < n:
            stack.append("(")
            backtrack(openN+1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN+1)
            stack.pop()
    backtrack(0,0)

    return res