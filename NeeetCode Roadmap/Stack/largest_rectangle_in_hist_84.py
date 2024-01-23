def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    maxArea = 0
    stack = []
    for i, h in enumerate(heights):
        start = i
        while stack and  stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height* (i-index))
            start = index
        stack.append((start,h))
    while stack:
        index, height = stack.pop()
        maxArea = max(maxArea, height * (len(heights)-index))
    return maxArea
        