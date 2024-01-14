def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    res = [0]*len(temperatures)
    stack = []
    
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            temp, index = stack.pop()
            res[index] = i - index
        stack.append((t,i))
    return res