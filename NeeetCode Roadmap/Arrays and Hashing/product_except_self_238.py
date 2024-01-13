def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    results = [0]*n
    prefix = 1
    for i in range(n):
        results[i] = prefix
        prefix = prefix*nums[i]
    
    postfix = 1
    for i in range(n-1,-1,-1):
        results[i] *= postfix
        postfix *= nums[i]
    
    return results