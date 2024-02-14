from collections import deque

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = []
    stack = deque()

    l = 0
    for r in range(len(nums)):
        while stack and stack[-1] < nums[r]:
            stack.pop()
        stack.append(nums[r])

        if r+1 >= k:
            res.append(stack[0])
            if stack and stack[0] == nums[l]:
                stack.popleft()
            l += 1
    return res